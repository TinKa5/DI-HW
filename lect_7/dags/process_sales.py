from datetime import datetime
import os
import json

from airflow import DAG
from airflow.models import Variable
from airflow.providers.http.operators.http import SimpleHttpOperator

date = "{{ ds }}"
raw_dir = os.path.join(Variable.get("BASE_DIR"), "raw", "sales", date)
stg_dir = os.path.join(Variable.get("BASE_DIR"), "stg", "sales", date)


dag = DAG(
    dag_id='process_sales',
    schedule_interval='0 1 */1 * *',
    start_date=datetime(2022, 8, 9),
    end_date=datetime(2022, 8, 12),
    catchup=True
)


task_extract_data_from_api = SimpleHttpOperator(
    task_id='extract_data_from_api',
    dag=dag,
    method='POST',
    http_conn_id='extract_data_conf',
    endpoint='/',
    headers={"Content-Type": "application/json"},
    data=json.dumps({"date": date, "raw_dir": raw_dir})
)

task_convert_to_avro = SimpleHttpOperator(
    task_id='convert_to_avro',
    dag=dag,
    method='POST',
    http_conn_id='convert_to_avro_conf',
    endpoint='/',
    headers={"Content-Type": "application/json"},
    data=json.dumps({"raw_dir": raw_dir, "stg_dir": stg_dir})
)

task_extract_data_from_api >> task_convert_to_avro
