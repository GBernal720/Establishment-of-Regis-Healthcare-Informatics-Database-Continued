import os, psycopg2, touch
from info import *

from datetime import datetime
root="C:\Users\eltac\Desktop\Regis_Homework\Test_Folder"



def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


for file in files(root+'\\Archive' ):
    csvfile = file
    name = csvfile.replace(".csv", "")
    fullpath = (root+'\\Archive' + '\\' + csvfile)
    dt = datetime.fromtimestamp(os.stat(fullpath).st_ctime)
    today = datetime.now()
    date_diff = today - dt

    print(csvfile)
    print (name)
    print (fullpath)
    print(date_diff)

    if date_diff.days > 9:
        print("File greater than 9 Days")
        connection = psycopg2.connect(user=User, password=Password, host=Host, port=Port, database=Database)
        cursor = connection.cursor()
        cursor.execute('Drop table ' + name)
        connection.commit()
        print("Table dropped PostgreSQL ")
        cursor.close()
        connection.close()
        os.remove(fullpath)
    else:
        print("File less than 9 days")

touch.touch(root+'\\landing\\'+'Database_Governance.trig')

