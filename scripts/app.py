"""
Aplicação Flask para a auditoria de perfis em redes sociais.
--- ARQUITETURA ---
1. O que ele faz:
   - Atua na camada de Apresentação (A) do pipeline de dados, fornecendo uma interface web para auditar perfis de redes sociais.
2. O impacto dele no projeto:
    - Permite que auditores humanos interajam com os dados, fornecendo feedback sobre perfis de redes sociais.
    - Facilita a coleta de informações adicionais (notas) sobre cada perfil auditado.
3. A Evolução (De Script para Aplicação Web):
    - Inicialmente, a auditoria era feita manualmente em um script de linha de comando
    - Agora, a aplicação Flask fornece uma interface web amigável, permitindo que múltiplos auditores trabalhem simultaneamente.
    - Facilidade em pessoas sem tanto conhecimento técnico possam auditar perfis de redes sociais.
"""

import os
from flask import Flask, render_template, jsonify, request
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Ajusta o template_folder para apontar para a pasta templates na raiz do projeto
app = Flask(__name__, template_folder='../templates')

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "social_audit_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432")
}
# Redes sociais que serão abertas, remover ou adicionar aqui conforme necessário.
SOCIAL_PLATFORMS = {
    "X (Twitter)": "https://x.com/{handle}",
    "GitHub": "https://github.com/{handle}",
    "Instagram": "https://instagram.com/{handle}",
    "LinkedIn": "https://linkedin.com/in/{handle}"
}

class ProfileRepository:
    """Isola as operações de base de dados utilizando POO."""
    def __init__(self, config):
        self.config = config

    def _get_conn(self):
        return psycopg2.connect(**self.config)

    def get_next_pending(self):
        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, screen_name FROM profiles WHERE status = 'PENDING' ORDER BY id ASC LIMIT 1;"
                )
                return cur.fetchone()

    def update_status(self, profile_id, status, notes):
        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE profiles SET status = %s WHERE id = %s;", (status, profile_id))
                cur.execute("INSERT INTO audit_logs (profile_id, notes) VALUES (%s, %s);", (profile_id, notes))
            conn.commit()

    def reset_all_profiles(self):
        """Reseta o status de todos os perfis para PENDING (para efeitos de teste)."""
        with self._get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE profiles SET status = 'PENDING';")
            conn.commit()

repo = ProfileRepository(DB_CONFIG)

@app.route("/")
def index():
    return render_template("index.html", platforms=SOCIAL_PLATFORMS)

@app.route("/api/next", methods=["GET"])
def api_next():
    profile = repo.get_next_pending()
    if not profile:
        return jsonify({"done": True})
    
    pid, handle = profile
    urls = {name: url.format(handle=handle) for name, url in SOCIAL_PLATFORMS.items()}
    return jsonify({"done": False, "id": pid, "screen_name": handle, "urls": urls})

@app.route("/api/complete", methods=["POST"])
def api_complete():
    data = request.json
    repo.update_status(data["id"], data["status"], data["notes"])
    return jsonify({"success": True})

@app.route("/api/reset", methods=["POST"])
def api_reset():
    repo.reset_all_profiles()
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True, port=5000)