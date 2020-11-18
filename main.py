import SQL.sql_reader as sql
import Utils.path as up

sql = sql.SQL()

route = up.route()

path_to_save = route.check_if_exist()

sql_scripts = route.sql_files()



for script in sql_scripts:
    #name = script + up.date_yesterday()
    name = script.split('.')[0][3:] + ' ' + up.date_yesterday()
    sql_text = sql.reader(script)
    print('Baixando ' + name)
    df = sql.execute(sql_text)
    print('Salvando ' + name)
    sql.df_to_xlsx(df,path_to_save, name)
    print('Finalizado')
    print()
    input('Pressione qualquer tecla para continuar')

print("Donwloads finalizados. Não esqueça de ajustar as datas nos arquivos finais")
print('Pressione qualquer tecla para finalizar')
input()

