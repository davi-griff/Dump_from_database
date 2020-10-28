import codecs
from codecs import open
import psycopg2
import pathlib

#sqlfile = "SQL/redicrim.sql"
#sql = open(sqlfile, mode='r', encoding='utf-8-sig').read()

#print(sql)

'''

conn = psycopg2.connect(
                dbname = "Leitura_Diaria",
                host="192.168.0.251",
                user='postgres',
                password='coest1',
                port="5432")


where = pathlib.Path.cwd() / 'FILES'
print(where)


periodo = '01.01 - 2020.10.26'

if pathlib.Path(where / periodo).exists():
    path_to_save = where / periodo
    print(path_to_save)
else:
    pathlib.Path.mkdir(where / periodo)

list_of_files = []

try_to_see = pathlib.Path(pathlib.Path.cwd()/'SQL'/'SQL_SCRIPTS')

for file in try_to_see.iterdir():
    file = pathlib.Path(file).name
    list_of_files.append(file)

print(list_of_files)

for name in list_of_files:
    print(name)

'''