from defs import *
from utils import *

def reset_DB():
    with psycopg.connect("dbname=project_database user=postgres password=1234") as database:
        with database.cursor() as cursor:
            for i in range(len(tables)):
                cursor.execute(f"DROP TABLE IF EXISTS {tables[i]} CASCADE")
            with open("DDL.sql", "r") as ddl_file:
                ddl_script = ddl_file.read()
                cursor.execute(ddl_script)
            database.commit()
            database.commit()

def populate_db():
    with psycopg.connect("dbname=project_database user=postgres password=1234") as database:
        with database.cursor() as cursor:
            for i in range(len(csv_filenames)):
                with open(f"csv_records/{csv_filenames[i]}.csv", "r", encoding='utf-8') as file:
                    header = file.readline()
                with cursor.copy(f"COPY {tables[i]} ({header}) FROM STDIN WITH CSV HEADER") as copy:
                    with open(f"csv_records/{csv_filenames[i]}.csv", "r", encoding='utf-8') as file:
                        copy.write(file.read())
                        print("Inserted csv data into: ", tables[i])

def main():
    start_time = time.time()
    reset_DB()
    populate_db()
    end_time = time.time()
    print("Time taken to populate the database: ", end_time - start_time, 'seconds')
main()