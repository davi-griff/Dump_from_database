from pathlib import Path
import codecs
from codecs import open
from datetime import datetime,timedelta


def date_yesterday():
    return '01.01 ATE ' + (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')

#print(date_yesterday())

class route():

    where = (Path.cwd() / 'FILES')

    date = date_yesterday()

    def __init(self,where,date):
        self.where = where
        self.date = date

    def check_if_exist(self):
        if Path(self.where / self.date).exists():
            path_to_save = self.where / self.date
            return path_to_save
        else:
            Path.mkdir(self.where / self.date)
            path_to_save = self.where / self.date
            return path_to_save

    def sql_files(self):
        list_of_files = []
        catch_files_on_dir = Path(Path.cwd()/'SQL'/'SQL_SCRIPTS')

        for file in catch_files_on_dir.iterdir():
            file = Path(file).name
            list_of_files.append(file)

        return list_of_files

