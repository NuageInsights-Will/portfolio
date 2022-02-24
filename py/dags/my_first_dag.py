"""
## Maintainer
William T. -- Junior Data Engineer @ NuageInsights

## Description
A simple DAG to get my feet wet in Airflow.
This DAG will run a BASH command that displays the file in a directory, 
and run a Python script that will retrieve some data and upload it to a SQL database.

## Documentation
--
"""

from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pandas as pd
import sqlite3

def check_connection(database: str):
    connection = sqlite3.connect(database)
    connection.close()

def upload_data(database: str):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS zillow_cleaned")
    cursor.execute("CREATE TABLE zillow_cleaned (IndexNum INTEGER PRIMARY KEY, LivingSpace_sq_ft INTEGER, Beds INTEGER, Baths FLOAT, YearBuilt INTEGER, ListPrice_dollars INTEGER, LivingSpaceGreaterThan2000 BOOLEAN, TotalRooms FLOAT, ListPriceInclTax FLOAT, EstMortgageFees FLOAT);")
    data = pd.read_csv('airflow/dags/zillow_cleaned.csv', index_col = 0)
    data.columns = ["LivingSpace_sq_ft", "Beds", "Baths", "YearBuilt", "ListPrice_dollars", "LivingSpaceGreaterThan2000", "TotalRooms", "ListPriceInclTax", "EstMortgageFees"]
    data.to_sql('zillow_cleaned', connection, if_exists='append', index=False)
    connection.commit()
    connection.close()

def finish(text: str) -> str:
    print(text)


with DAG(
        dag_id="my_first_dag",
        start_date=datetime(2022, 2, 23),
        schedule_interval=timedelta(days=1),
        catchup=True,
        max_active_runs=1,
        dagrun_timeout=timedelta(minutes=5),        
        on_failure_callback=None,
        on_success_callback=None,
        tags=["beginner"],
        doc_md=__doc__,
    ) as dag:

    start = BashOperator(
        task_id="start",
        bash_command="echo starting..."
        )

    run_this = BashOperator(
        task_id="run_this",
        bash_command="ls"
        )
    
    also_run_this = PythonOperator(
        task_id="also_run_this",
        python_callable=check_connection,
        op_kwargs={"database" : "online_store.db"}
    )

    next_run_this = PythonOperator(
        task_id="next_run_this",
        python_callable=upload_data,
        op_kwargs={"database" : "online_store.db"}
    )

    end = PythonOperator(
        task_id="end",
        python_callable=finish,
        op_kwargs= {"text" : "Finished!"}
    )

    start >> [run_this, also_run_this] >> next_run_this >> end

