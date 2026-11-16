# Social Profile Audit & Data Pipeline

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Data%20Engineering-Pipeline-22D3EE?style=for-the-badge" alt="Data Pipeline" />
</p>

An enterprise-grade data ingestion and operational workflow utility designed to manage, track, and audit targeted user profiles. Transitioned from a local flat-file script to a robust relational data architecture powered by **PostgreSQL** inside **Docker**, ensuring state persistence, structured logging, and transactional integrity.

---

## Architecture & Core Features

- **Containerized Relational Database**: Deploys a persistent PostgreSQL instance via Docker, featuring custom `ENUM` types, foreign key constraints (`ON DELETE CASCADE`), and transactional audit logs.
- **Automated Seeding & ETL**: Programmatic ingestion pipeline that seeds relational tables with handles, avoiding duplication via `ON CONFLICT` clauses.
- **Stateful Audit Workflow**: Manages profile states (`PENDING`, `IN_PROGRESS`, `COMPLETED`, `FLAGGED`) to prevent redundant reviews.
- **Low-Overhead Automation**: Interacts with the operating system's default browser runtime (`webbrowser`) for rapid evaluation without heavy WebDriver footprints.

---

## Database Schema

The core PostgreSQL database (`social_audit_db`) is structured around two main relational tables:
1. **`profiles`**: Stores unique screen names, lifecycle status (`audit_status` ENUM), and creation timestamps.
2. **`audit_logs`**: Tracks operational history, foreign keys referencing profiles, timestamps, and audit notes.

---

## Prerequisites & Setup

Ensure you have **Docker Desktop** and **Python 3.x** installed on your machine.

### 1. Run PostgreSQL via Docker
Start the database container on port `5432`:

docker run --name postgres-audit -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres


### 2. Install Dependencies
Install the required Python packages:
Bash

pip install -r requirements.txt

### 3. Run the Ingestion Seed

Populate the database with initial profiles:
Bash

python scripts/ingest_csv.py

Technical Stack

    Database & Containerization: PostgreSQL 15+, Docker / WSL 2

    Data Manipulation: Pandas & NumPy

    Database Connectivity: Psycopg2-binary

    OS Interfacing: Native browser runtime integration
