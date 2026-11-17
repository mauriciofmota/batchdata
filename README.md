# Social Profile Audit & Data Dashboard

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Architecture-FullStack%20POO-22D3EE?style=for-the-badge" alt="FullStack Architecture" />
</p>

An enterprise-grade data ingestion and operational auditing web application designed to manage, track, and review targeted user profiles. Evolved from a local flat-file script into a robust **Full-Stack Web Dashboard** powered by **Flask**, object-oriented database repositories, and a persistent **PostgreSQL** instance running inside **Docker**.

---

## Architecture & Core Features

- **Full-Stack Web Interface**: Replaces terminal-bound execution with a responsive, dark-mode web dashboard (`localhost:5000`) featuring automated tab opening, status toggles, and instant queue resets for testing.
- **Object-Oriented Data Access (POO)**: Implements the Repository Pattern (`ProfileRepository`) to neatly isolate database operations and query logic from the presentation layer.
- **Containerized Relational Database**: Deploys a persistent PostgreSQL instance via Docker, featuring custom `ENUM` types, foreign key constraints (`ON DELETE CASCADE`), and transactional audit logs.
- **Automated Seeding & ETL**: Programmatic ingestion layer (`ingest_csv.py`) that processes tabular profile sources and sanitizes inputs before persistence.
- **Stateful Audit Workflow**: Manages granular profile lifecycle states (`PENDING`, `IN_PROGRESS`, `COMPLETED`, `FLAGGED`) to prevent redundant reviews and ensure data integrity.

---

## Project Structure

Database Schema

The core PostgreSQL database (social_audit_db) is structured around two main relational tables:

    profiles: Stores unique screen names, lifecycle status, and creation timestamps.

    audit_logs: Tracks operational history, foreign keys referencing profiles, timestamps, and audit notes.

Prerequisites & Setup

Ensure you have Docker Desktop and Python 3.x installed on your machine.
1. Run PostgreSQL via Docker

Start the database container on port 5432:
Bash

docker run --name postgres-audit -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres

2. Configure Environment Variables

Create a .env file in the root directory with your database configurations:
Code snippet(JUST A .ENV MODEL)

DB_NAME=social_audit_db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

3. Install Dependencies

Install the required Python packages:
Bash

pip install -r requirements.txt

4. Run the Ingestion & Start the Web App

Populate the database with initial profiles and launch the Flask dashboard:
Bash

python scripts/ingest_csv.py
python scripts/app.py

Open your browser and navigate to http://127.0.0.1:5000 to interact with the audit dashboard!
Technical Stack

    Backend & Web Framework: Python 3.x, Flask

    Database & Containerization: PostgreSQL 15+, Docker

    Data Manipulation & Config: Pandas, NumPy, Python-Dotenv, Psycopg2-binary

    Frontend: HTML5, Modern CSS3 (Dark Theme), Vanilla JavaScript
