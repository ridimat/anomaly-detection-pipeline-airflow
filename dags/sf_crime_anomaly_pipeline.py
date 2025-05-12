from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd
from sklearn.ensemble import IsolationForest

#task 1 - fetch real-time data
def fetch_public_safety_data():
    url = "https://data.sfgov.org/resource/cuks-n6tp.json"
    response = requests.get(url)
    data = response.json()
    df = pd.json_normalize(data)
    df.to_csv("/opt/airflow/dags/public_data.csv", index=False)
    print("✅ Data saved!")

#task 2 - detect anomalies
def detect_anomalies():
    df = pd.read_csv("/opt/airflow/dags/public_data.csv")
    df = df.dropna(subset=['location.coordinates'])
    df[['x', 'y']] = df['location.coordinates'].str.strip("[]").str.split(",", expand=True).astype(float)
    model = IsolationForest(contamination=0.01, random_state=42)
    df['anomaly'] = model.fit_predict(df[['x', 'y']])
    anomalies = df[df['anomaly'] == -1]
    anomalies.to_csv("/opt/airflow/dags/anomalies.csv", index=False)
    print(f"🚨 {len(anomalies)} anomalies detected and saved!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id="sf_crime_anomaly_pipeline",
    schedule_interval="@hourly",
    default_args=default_args,
    catchup=False
) as dag:
    fetch_data = PythonOperator(
        task_id="fetch_public_safety_data",
        python_callable=fetch_public_safety_data
    )

    detect_anomaly = PythonOperator(
        task_id="detect_anomalies",
        python_callable=detect_anomalies
    )

    fetch_data >> detect_anomaly
