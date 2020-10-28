from environs import Env
import pandas as pd
import psycopg2 as psql
import codecs
from codecs import open
import pathlib

class SQL():

    current_path = pathlib.Path.cwd()

    env = Env()

    env.read_env()

    sql_ip = env("SQL_IP")
    sql_loggin = env("SQL_LOGGIN")
    sql_password = env("SQL_PASSWORD")
    sql_port = env("SQL_PORT")
    sql_table = env("SQL_TABLE") 

    def __init(self, sql_ip,sql_loggin,sql_password,sql_port,sql_table,current_path):
        self.sql_ip = sql_ip
        self.sql_loggin = sql_loggin
        self.sql_password=sql_password
        self.sql_port = sql_port
        self.sql_table=sql_table
        self.path = current_path

    def reader(self,sql_option):
        sql_url = sql_option
        sql_txt = open(f'SQL/SQL_SCRIPTS/{sql_url}', 'r', 'utf-8').read()
        return sql_txt

    def connection(self):
        try:
            conn = psql.connect(
                host=self.sql_ip,
                user=self.sql_loggin,
                dbname=self.sql_table,
                password=self.sql_password,
                port=self.sql_port
            )
            return conn
        except:
            print("Unable to connect to the database")

    def execute(self, query):
        conn = self.connection()
        df = pd.read_sql_query(query,conn)
        return df

    def df_to_xlsx(self, df,path, name):
        with pd.ExcelWriter(f'{path}/{name}.xlsx',engine='xlsxwriter', datetime_format='%d/%m/%Y',date_format='%d/%m/%Y') as writer:
            df.to_excel(writer,index=False,encoding='utf-8')
