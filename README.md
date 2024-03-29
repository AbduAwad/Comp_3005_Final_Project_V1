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