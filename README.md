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

PostgreSQL (optional extension)
