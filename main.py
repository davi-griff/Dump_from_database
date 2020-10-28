import SQL.sql_reader as sql
import Utils.path as up

sql = sql.SQL()

route = up.route()

path_to_save = route.check_if_exist()

sql_scripts = route.sql_files()



for script in sql_scripts:
    name = script + up.date_yesterday()
    sql_text = sql.reader(script)
    print('Baixando')
    df = sql.execute(sql_text)
    print('Salvando')
    sql.df_to_xlsx(df,path_to_save, name)


