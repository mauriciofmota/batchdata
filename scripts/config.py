"""
Módulo: Segurança e Configuração do Banco de Dados
--- ARQUITETURA ---
1. O que ele faz:
    - Carrega variáveis de ambiente do arquivo .env para configurar a conexão com o banco de dados.
    - Garante que a senha do banco de dados esteja definida, evitando falhas silenciosas.
2. O impacto dele no projeto:
    - Centraliza a configuração do banco de dados, tornando o código mais limpo e seguro.
    - Facilita a mudança de credenciais sem alterar o código-fonte.
3. A Evolução (De Hardcoded para Variáveis de Ambiente):
    - Inicialmente, as credenciais do banco de dados estavam hardcoded no código, o que é inseguro.
    - Agora, elas são carregadas de variáveis de ambiente, permitindo maior flexibilidade e segurança.
"""
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "social_audit_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432")
}

if not DB_CONFIG["password"]:
    raise ValueError("Erro Crítico: A variável de ambiente DB_PASSWORD não está definida!")