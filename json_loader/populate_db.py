from defs import *
from utils import *

# UPDATE THESE LISTS:
DB_index_list = ['Shots_idx', 'Shots_idx2']
DB_partition_list = ['Shots_2018_2019', 'Shots_2019_2020', 'Shots_2020_2021', 'Shots_2003_2004', 'First_time_shots_2018_2019', 'First_time_shots_2018_2019_f', 'First_time_shots_2019_2020', 'First_time_shots_2019_2020_f', 'First_time_shots_2020_2021', 'First_time_shots_2020_2021_f']


def reset_DB():
    with psycopg.connect("dbname=project_database user=postgres password=1234") as database:
        with database.cursor() as cursor:
            for i in range(len(DB_index_list)):
                cursor.execute(f"DROP INDEX IF EXISTS {DB_index_list[i]}")
            for i in range(len(DB_partition_list)):
                cursor.execute(f"DROP TABLE IF EXISTS {DB_partition_list[i]} CASCADE")
            for i in range(len(tables)):
                cursor.execute(f"DROP TABLE IF EXISTS {tables[i]} CASCADE")
                
            with open("DDL.sql", "r") as ddl_file:
                ddl_script = ddl_file.read()
                cursor.execute(ddl_script)
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