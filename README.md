# anomaly-detection-pipeline-airflow
🚨 Anomaly Detection Pipeline using Apache Airflow
This project automates the end-to-end pipeline of fetching real-time public safety data, detecting geographic anomalies, and storing the results — all orchestrated using Apache Airflow and containerized with Docker.

🧠 What It Does
Fetches public safety incident data hourly from San Francisco's open data API

Cleans and processes the data using Python

Applies Isolation Forest (Scikit-learn) to detect anomalies based on latitude & longitude

Stores both clean and anomalous records into CSV files (or PostgreSQL optionally)

Runs entirely through scheduled tasks in Airflow, isolated inside Docker containers

🛠 Tech Stack
Python

Apache Airflow

Docker

Scikit-learn

Pandas

Public API

PostgreSQL (optional extension


⚙️ Setup Instructions
Make sure Docker Desktop is running.

1. Clone the Repository
   git clone https://github.com/your-username/anomaly-detection-pipeline-airflow.git
   cd anomaly-detection-pipeline-airflow
2. Build Docker Containers
   docker-compose build --no-cache
3. Start Airflow
   docker-compose up -d
   Access Airflow UI at: http://localhost:8080
Default login:
Username: admin
Password: admin

📌 Running the DAG
Turn the DAG switch ON in Airflow UI

Trigger manually or wait for the hourly schedule

View task logs and DAG graph for output

📂 Output Files
Generated inside the /dags folder:

public_data.csv: Cleaned and structured input data

anomalies.csv: Records with detected spatial anomalies




