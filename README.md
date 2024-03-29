# Comp_3005_Final_Project_V1

### Name & Student Number:

- Name: Abdulrahman Awad
- Student Number: 101256090

___

### Pushing files to git:

**For the first time only:**
- execute the following command in a linux terminal to make the push.sh file executable:
```bash
chmod +x push.sh
```

**After this:**
- To push, simply enter the command:
```bash
./push.sh "commit message"
```


### Load Initial Data:

To load the initial information such as as all the data files that are parsed and saved into csv files, run the following command in the terminal:

1. Navigate to the directory where the loader folder is located.
```bash
cd json_loader
```
2. Run the following command to load the initial data.
```bash
python loader.py
```

### Connect and load the data into the database:

To connect to the database and insert the data into the database tables run the following command in the terminal:

1. Navigate to the directory where the loader folder is located.
```bash
cd json_loader
```
2. Run the following command to connect and load the data into the database.
```bash
python postgres_import.py
```

### Query the database:

There are 10 queries that can be run to get the results from the database. each .py file in the scripts folder is a query that can be run to get the results.

To query the database and get the results, first cd into scripts folder and then run the following command in the terminal:

1. Navigate to the directory where the scripts folder is located.
```bash
cd scripts
```
2. To run the first query which gets In the La Liga season of 2020/2021, sort the players from highest to lowest based on their
average xG scores.

```bash
python Q_1.py
```

3. To run the second query which gets In the La Liga season of 2020/2021, sort the players from highest to lowest based on most shots
taken.

```bash
python Q_2.py
```

4. To run the third query which gets n the La Liga seasons of 2020/2021, 2019/2020, and 2018/2019 combined, find the players with
the most first-time shots. Sort them from highest to lowest

```bash
python Q_3.py
```

5. To run the 4th query which gets in the La Liga season of 2020/2021, find the teams with the most passes made. Sort them from
highest to lowest

```bash
python Q_4.py
```

6. To run the 5th query which gets In the Premier League season of 2003/2004, find the players who were the most intended
recipients of passes. Sort them from highest to lowest.

```bash
python Q_5.py
```

7. To run the 6th query which gets In the Premier League season of 2003/2004, find the teams with the most shots made. Sort
them from highest to lowest.

```bash
python Q_6.py
```

8. To run the 7th query which gets In the La Liga season of 2020/2021, find the players who made the most through balls. Sort
them from highest to lowest.

```bash
python Q_7.py
```

9. To run the 8th query which gets In the La Liga season of 2020/2021, find the teams that made the most through balls. Sort
them from highest to lowest.

```bash
python Q_8.py
```

10. To run the 9th query which gets In the La Liga seasons of 2020/2021, 2019/2020, and 2018/2019 combined, find the players that
were the most successful in completed dribbles. Sort them from highest to lowest.

```bash
python Q_9.py
```

11. To run the 10th query which gets In the La Liga season of 2020/2021, find the players that were least dribbled past. Sort them
from lowest to highest.

```bash
python Q_10.py
```

### Query Output:

The output of the queries will be saved in the scripts folder as csv files. The files will be named Q_x.csv where x is the query number.


### Install the required packages:

```bash
pip install --upgrade pip           # upgrade pip to at least 20.3
pip install "psycopg[binary]"       # remove [binary] for PyPy
```

### Change ur password for postgres to 1234
```bash
psql -U postgres
```
```bash
postgres=# ALTER USER postgres WITH PASSWORD '1234';
ALTER ROLE
```


## ABDU's JOB
Create DB dump for dbexport.sql: (FOR ABDU)

- Anytime we modify the database we must create a new dump and save it in the dbexports.sql file

```bash
pg_dump.exe --file "C:\\Users\\sheri\\Documents\\db_dump.sql" --host "localhost" --port "5432" --username "postgres" --verbose --format=p "project_database"
```

Path to abdu dump file:
```bash
C:\Users\sheri\Documents\db_dump.sql
```

### Run the autograder for Abdulrahman Awad:

Install postgers on the vm (already done):
run the script.sh to intsall postgres

```bash
chmod +x script.sh
./script.sh
```

To run autograder dont change anything just run it in the vm but change the host in the queries.py to your hosts ip address mine is 10.0.0.34, make sure to configure your host machine to recieve and be a host 

```bash
python queries.py
```

## BEFORE SUBMISSION:

Change host in queries.py back to localhost

```bash 
host = "localhost"
```