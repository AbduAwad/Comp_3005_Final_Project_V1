import psycopg
import time
import csv

def q_1():
    with psycopg.connect("dbname=project_database user=postgres password=1234") as database:
        with database.cursor() as cursor:
            start_time = time.time()
            cursor.execute("""
                SELECT player_name, AVG(statsbomb_xg) as avg_xg_score
                FROM Shots s
                WHERE season_name = '2020/2021'
                    AND competition_name = 'La Liga'
                    AND statsbomb_xg > 0
                GROUP BY player_name
                ORDER BY avg_xg_score DESC
            """)
            end_time = time.time()
            print("Time taken to execute query 1: ", end_time - start_time, 'seconds')
            result = cursor.fetchall()
    
    with open('Q_1.csv', 'w', encoding='utf-8', newline='') as file: # write the output to a csv file called Q_1.csv
        writer = csv.writer(file)
        writer.writerow(["player_name", "avg_xG"])
        for row in result:
            player_name = row[0]
            avg_xG = row[1] 
            writer.writerow([player_name] + [avg_xG])

def q_2():
    with psycopg.connect("dbname=project_database user=postgres password=1234") as database:
        with database.cursor() as cursor:
            start_time = time.time()
            cursor.execute("""
                SELECT player_name, COUNT(*) as num_shots
                FROM Shots
                WHERE season_name = '2020/2021'
                    AND competition_name = 'La Liga'
                GROUP BY player_name
                HAVING COUNT(*) > 0
                ORDER BY num_shots DESC
            """)
            end_time = time.time()
            print("Time taken to execute query 2: ", end_time - start_time, 'seconds')
            result = cursor.fetchall()
    
    with open('Q_2.csv', 'w', encoding='utf-8', newline='') as file: # write the output to a csv file called Q_1.csv
        writer = csv.writer(file)
        writer.writerow(["player_name", "num_shots"])
        for row in result:
            player_name = row[0]
            num_shots = row[1] 
            writer.writerow([player_name] + [num_shots])

def q_3():
    with psycopg.connect("dbname=project_database user=postgres password=1234") as database:
        with database.cursor() as cursor:
            start_time = time.time()
            cursor.execute("""
                SELECT player_name, COUNT(*) first_time_shots
                FROM Shots
                WHERE season_name = '2020/2021' OR season_name = '2019/2020' OR season_name = '2018/2019'
                    AND competition_name = 'La Liga'
                    AND first_time = TRUE
                GROUP BY player_name
                HAVING COUNT(*) > 0
                ORDER BY first_time_shots DESC
            """)
            end_time = time.time()
            print("Time taken to execute query 3: ", end_time - start_time, 'seconds')
            result = cursor.fetchall()

    with open('Q_3.csv', 'w', encoding='utf-8', newline='') as file: # write the output to a csv file called Q_1.csv
        writer = csv.writer(file)
        writer.writerow(["player_name", "num_shots"])
        for row in result:
            player_name = row[0]
            num_shots = row[1] 
            writer.writerow([player_name] + [num_shots])







def main():
    q_1()
    q_2()

main()