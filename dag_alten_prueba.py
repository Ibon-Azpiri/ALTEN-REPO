from datetime import datetime, timedelta
from airflow import models
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

from funciones_dag import datos_api

url = "https://api.open-meteo.com/v1/forecast"

project_id = "proyecyo1"
table_name = "DATASET.tabla_meteo"


START_DATE = datetime(year=2026, month=5, day=18, hour=3, minute=0)

default_args = {
    'start_date': START_DATE,
    'retries': 2,
    'retry_delay': timedelta(minutes=15)
}

with models.DAG(
    "dag_alten_prueba",
    default_args=default_args,
    schedule='0 3 * * *',
    catchup=False
) as dag:

    task_datos_api = PythonOperator(
        task_id="datos_api",
        python_callable=datos_api.run,
        op_args=[url, project_id, table_name]
    )

    task_consulta_bq = BigQueryInsertJobOperator(
        task_id="consulta_bq",
        configuration={
            "query": {
                "query": "{% include 'funciones_dag/consulta_dag.sql' %}",
                "useLegacySql": False
            }
        }
    )

task_datos_api >> task_consulta_bq
