import psycopg2

DB_CONFIG = {
    "dbname": "social_audit_db",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": "5432"
}

def seed_profiles():
    # Lista de perfis de exemplo para a auditoria
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