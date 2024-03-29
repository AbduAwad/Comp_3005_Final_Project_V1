import psycopg

def run_DDL():
    tables = [
        "Countrys", "Competitions", "Seasons", "Stadiums", "Referees", "Managers", 
        "Teams", "Matches", "Players", "TeamFormations", "GenericEvents", "Passes", 
        "Shots", "Dribbles", "BadBehaviours", "BallReciepts", "BallRecoverys", "Blocks", 
        "Carrys", "Clearances", "Duels", "FoulsCommitted", "FoulsWon", "GoalkeeperEvents", 
        "Interceptions", "Substitutions", "FreezeFrames", "DribbledPasts", "PlayerMinutes"
    ]
    with psycopg.connect("dbname=project_database user=postgres password=postgres") as database:
        with database.cursor() as cursor:
            for i in range(len(tables)):
                cursor.execute(f"DROP TABLE IF EXISTS {tables[i]} CASCADE")
            with open("Comp_3005_Final_Project_V1/json_loader/DDL.sql", "r") as file:
                ddl_script = file.read()
                cursor.execute(ddl_script)
            database.commit()

def populate_db():
    print("populating database...")

def main():
    run_DDL()
    populate_db()

main()