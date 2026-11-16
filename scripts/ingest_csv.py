"""
Módulo: Ingestão de Dados (Extract Layer)

--- ARQUITETURA ---
1. O que ele faz:
   - Atua na camada de Extração (E) do pipeline de dados, lendo dados brutos de ficheiros 
     externos em formato CSV e limpando valores nulos antes de persistir no banco.

2. O impacto dele no projeto:
   - Funciona como a porta de entrada para fontes de dados externas estáticas. 
     Garante que o pipeline não processe sujeira (como linhas vazias ou campos nulos).

3. A Evolução (De CSV para Lista em Python):
   - Embora o CSV seja ótimo para lotes iniciais, desacoplar a lógica de ingestão 
     de um ficheiro físico permite que o script receba dados diretamente de uma lista 
     em memória, de uma API REST ou de testes automatizados (Unit Tests).
4. Mudanças futuras:
   - Adicionar suporte a outros formatos de dados (JSON, Parquet, etc.).
   - Adicionar possibilidade tanto de escrever diretamente os valores nesse arquivo, quanto subir um arquivo externo.
-----------------------------------------------------
"""

import psycopg2

DB_CONFIG = {
    "dbname": "social_audit_db",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": "5432"
}

def seed_profiles():
    # Lista de perfis de exemplo para a auditoria, mude aqui se quiser adicionar ou remover perfis
    sample_users = [
        "dev_python_br",
        "dados_analise",
        "tech_lead_sp",
        "engenharia_dados",
        "pythonista_rio",
        "social_auditor"
    ]

    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    inserted = 0
    for user in sample_users:
        cursor.execute(
            """
            INSERT INTO profiles (screen_name)
            VALUES (%s)
            ON CONFLICT (screen_name) DO NOTHING;
            """,
            (user,)
        )
        inserted += cursor.rowcount

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Sucesso! {inserted} perfis iniciais inseridos diretamente no PostgreSQL.")

if __name__ == "__main__":
    seed_profiles()