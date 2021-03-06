from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
#from airflow.operators import MultiplyBy5Operator

def print_hello():
 return 'Hello World'
    
dag = DAG('bavani_id', description='Hello world example', schedule_interval='0 12 * * *', start_date=datetime(2017, 3, 20), catchup=False)
dummy_operator = DummyOperator(task_id='dummy_task', retries = 3, dag=dag)
hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)
dummy01_operator = DummyOperator(task_id='dummy_task_15', retries = 3, dag=dag)
dummy01_operator >> hello_operator
