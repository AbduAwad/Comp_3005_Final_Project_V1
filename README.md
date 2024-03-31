# Comp_3005_Final_Project_V1

### Name & Student Number:

- Name: Abdulrahman Awad
- Student Number: 101256090

___

### Install the required packages:

```bash
pip install --upgrade pip           # upgrade pip to at least 20.3
pip install "psycopg[binary]"       # remove [binary] for PyPy
```
___
### Change ur password for postgres to 1234
```bash
psql -U postgres
```
```bash
postgres=# ALTER USER postgres WITH PASSWORD '1234';
ALTER ROLE
```
___

### STEP 1. Create the database:

1.  Create a database called "project_database" in PostgreSQL.


___
### STEP 2: Parse JSON DATA (only necessary once) 
#### *Submission already has parsed json data and created the csv files  so this step is not necessary

- To parse the json data and place the data into csv files where the records in 
each csv file will be copied directly into a table in the database, run the following command:

1. Navigate to the json_loader folder
```bash
cd json_loader
```

2. Run the following command to parse the json data and place the data into csv files:
```bash
python json_parser.py
```


___

### STEP 3. Create the tables and load the data into the database:

run the following command to load the data into the database tables

```bash
python populate_db.py
```
____
### STEP 3. Run the autograder:










### FILE STRUCTURE AND DESCRIPTIONS:

- **Folder**: json_loader: Contains the json files and the python script to load the data into the database tables.
    - **Folder**: **competitions_data**: Contains the json files for the competitions.
    - **Folder**: **events_data**: Contains the json files for the events for each match.
    - **Folder**: **lineups_data**: Contains the json files for the lineups for each match.
    - **Folder**: **matches_data**: Contains the json files for the matches.

    - **File**: **download_jsons.py**: Personal Python script to download the json files from github and place them in events_data and lineups_data folders.

- **File**: **push.sh**: Bash script to push the files to git.
- **File**: **README.md**: This file.
- **File**: **DDL.sql**: SQL script to create the tables for the database.
- **File**: **queries.py**: Python script to run the autograder for Abdulrahman Awad.

### BONUES QUERIES:

#### Bonus Query 1:

#### Bonus Query 2:

#### VIDEO DEMONSTRATION:

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


## TESTER AND DB DUMP INFO
Create DB dump for dbexport.sql:

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