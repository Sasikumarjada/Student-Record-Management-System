# Student-Record-Management-System
<img width="1305" height="695" alt="image" src="https://github.com/user-attachments/assets/7b6cd19c-f9a6-4b01-b453-1440b21e4d3c" />

A simple RESTful Student Management API built with Flask and MySQL, containerized with Docker, and deployable to an AWS EC2 instance using GitHub Actions.

Features:
- CRUD endpoints for Student
  - POST /student
  - GET /students
  - GET /student/<id>
  - PUT /student/<id>
  - DELETE /student/<id>

Tech stack:
- Python, Flask, Flask-SQLAlchemy
- MySQL (can run via Docker or external RDS)
- Docker + docker-compose
- GitHub Actions for CI/CD
- Deployment over SSH to an EC2 instance

Quick start (local, with docker-compose)
1. Copy the repo locally.
2. Start services:
   ```bash
   docker compose up --build
   ```
3. API is available at http://localhost:5000

Environment variables used (examples)
- MYSQL_HOST — host of MySQL (default: db for local compose)
- MYSQL_PORT — 3306
- MYSQL_DATABASE — students_db
- MYSQL_USER — student_user
- MYSQL_PASSWORD — student_pass

GitHub Actions CI/CD (deploy to EC2)
This repo includes `.github/workflows/deploy.yml` which will:
- Run on push to `main`
- Copy files to the EC2 host over SCP
- SSH into EC2 and run `deploy.sh` to build & start the container

Secrets required for the workflow
- EC2_HOST — the public IP or DNS of your EC2 instance
- EC2_USER — the SSH user (e.g., ubuntu)
- EC2_SSH_KEY — the SSH private key (use GitHub Actions secret)
- EC2_SSH_PORT — optional (default 22)

On the EC2 instance
- Install Docker & Docker Compose
- Make sure the SSH user in workflow can run docker / docker-compose
- Optionally create a `.env` in the deployment directory with your DB credentials or ensure the deployment points to an existing RDS/MySQL.

Security notes
- Do NOT store secret keys or DB passwords in the repo.
- Use GitHub Secrets for all private values and the SSH key.
- Open the necessary ports (22 for SSH during deploy, 5000 for app if you want public access) in your EC2 security group.

Next steps / suggestions
- Add unit & integration tests + a GitHub Actions test workflow
- Add health and readiness endpoints
- Add HTTPS / reverse proxy (nginx) in front of the app
- Use a remote/managed MySQL (RDS) for production
