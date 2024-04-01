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








___

### FILE STRUCTURE AND DESCRIPTIONS:

- **Folder**: json_loader: Contains the json files and the python script to load the data into the database tables.
    - **Folder**: **competitions_data**: Contains the json files for the competitions.
    - **Folder**: **events_data**: Contains the json files for the events for each match.
    - **Folder**: **lineups_data**: Contains the json files for the lineups for each match.
    - **Folder**: **matches_data**: Contains the json files for the matches.

    - **File**: **download_jsons.py**: Personal Python script to download the json files from github and place them in events_data and lineups_data folders.
    - **File**: **DDL.sql**: SQL script to create the tables for the database.

- **Folder**: readme_images: Contains the images used in the README file.
- **File**: **push.sh**: Bash script to push the files to git.
- **File**: **README.md**: This file.
- **File**: **queries.py**: Python script to run the autograder for Abdulrahman Awad.

____

### BONUS QUERIES:
____

[Open_Data_Events_v4.0.0.pdf](../../../../../Downloads/Open_Data_Events_v4.0.0.pdf)

____
#### **Bonus Query 1**: Divide the goal into 6 equal-size areas (top-left, top-middle, top-right, bottom-left, bottom-middle, and bottom-right). In the La Liga seasons of 2020/2021, 2019/2020, and 2018/2019 combined, find the players who shot the most in either the top-left or top-right corners. Sort them from highest to lowest.

![GOAL DIMENSIONS](readme_images/image.png)

##### CORNERS DIMENSIONS:
![alt text](readme_images/image-3.png)

AWAY GOAL DIMENSIONS:
COORDINATES ARE THE SAME, except x is 0 instead of 120

Now that we know the coordinates of the top right and left corners, we can find the players who shot the most in either of these corners. by constrructing the query where the x,y,z location of the shot is within the range of the top right or left corners.

#### SQL Query for Bonus Query 1:
```sql  
SELECT player_name, COUNT(*) as num_shots_top_corners
    FROM Shots
    WHERE season_name IN ('2018/2019', '2019/2020', '2020/2021')
        AND competition_name = 'La Liga'
        AND ((end_location_x = 120 AND end_location_y BETWEEN 36 AND 38.67 AND end_location_z BETWEEN 1.33 AND 2.67)
        OR (end_location_x = 120 AND end_location_y BETWEEN 41.33 AND 44 AND end_location_z BETWEEN 1.33 AND 2.67)
        OR (end_location_x = 0 AND end_location_y BETWEEN 36 AND 38.67 AND end_location_z BETWEEN 1.33 AND 2.67)
        OR (end_location_x = 0 AND end_location_y BETWEEN 41.33 AND 44 AND end_location_z BETWEEN 1.33 AND 2.67))
    GROUP BY player_name
    HAVING COUNT(*) > 0
    ORDER BY num_shots_top_corners DESC
```
____ 

#### Bonus Query 2: In the La Liga season of 2020/2021, find the teams with the most successful passes into the box. Sort them from the highest to lowest

![alt text](readme_images/image-4.png)

##### BOX COORDINATES:

BOX 1:
- x: 0 y: 62
- x: 0 y: 18
- x: 18 y: 18
- x: 18 y: 62

BOX 2:
- x: 102 y: 18
- x: 120 y: 18
- x: 120 y: 62
- x: 102 y: 62

Now that we have the x,y coordinates of the corners of the box, any pass that is succcesful and has a end_location within the box will be counted as a successful pass into the box. We can construct the query to find the teams with the most successful passes into the box by counting the number of successful passes that have an end_location within the box.

#### SQL Query for Bonus Query 2:
```sql
SELECT team_name, COUNT(*) as num_passes_into_box
    FROM Passes
    WHERE competition_name = 'La Liga'
        AND season_name = '2020/2021'
        AND (end_location_x >= 0 AND end_location_x <= 18 AND end_location_y >= 18 AND end_location_y <= 62
        OR end_location_x >= 102 AND end_location_x <= 120 AND end_location_y >= 18 AND end_location_y <= 62)
        AND outcome_name is NULL
    GROUP BY team_name
    HAVING COUNT(*) > 0
    ORDER BY num_passes_into_box DESC;
```

____

#### BONUS QUERIES VIDEO DEMONSTRATION:

LINK: https://youtu.be/lc0Kb12VGIc

____

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

___

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