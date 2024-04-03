-- DDL --

-- TO MAKE MORE EFFICIENT DECREASE SIZE OF VARCHAR COLUMNS AND USE ENUMS WHERE POSSIBLE
-- AN enum is a string object with a value chosen from a list of permitted values that are enumerated explicitly in the column specification at table creation time.

CREATE TABLE Countrys (
    country_id INT UNIQUE NOT NULL,
    country_name VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (country_name)
);

CREATE TABLE Competitions (
	competition_id INT UNIQUE NOT NULL,
	competition_name VARCHAR(255) NOT NULL,
    country_name VARCHAR(255) NOT NULL,
    competition_gender VARCHAR(255),
    competition_youth BOOLEAN,
    competition_international BOOLEAN,
	PRIMARY KEY (competition_id),
	FOREIGN KEY (country_name)
    	REFERENCES Countrys (country_name)
);

CREATE TABLE Seasons (
    season_id INT UNIQUE NOT NULL,
	competition_id INT NOT NULL,
	season_name VARCHAR(255) NOT NULL,
	PRIMARY KEY (season_id),
	FOREIGN KEY (competition_id)
		REFERENCES Competitions (competition_id)
);

CREATE TABLE Stadiums (
    stadium_id INT UNIQUE NOT NULL,
    stadium_name VARCHAR(255) NOT NULL,
    stadium_country_id int NOT NULL,
    PRIMARY KEY (stadium_id),
    FOREIGN KEY (stadium_country_id)
    	REFERENCES Countrys (country_id)
);

CREATE TABLE Referees (
    referee_id INT UNIQUE NOT NULL,
    referee_name VARCHAR(255) NOT NULL,
    referee_country_id int NOT NULL,
    PRIMARY KEY (referee_id),
    FOREIGN KEY (referee_country_id)
    	REFERENCES Countrys (country_id)
);

CREATE TABLE Managers (
    manager_id INT UNIQUE NOT NULL,
    manager_name VARCHAR(255) NOT NULL,
    manager_nickname VARCHAR(255),
    manager_dob DATE,
    manager_country_id int NOT NULL,
    PRIMARY KEY (manager_id),
    FOREIGN KEY (manager_country_id)
    	REFERENCES Countrys (country_id)
);

CREATE TABLE Teams (
    team_id INT UNIQUE NOT NULL,
    team_name VARCHAR(255) NOT NULL UNIQUE,
    team_gender VARCHAR(255),
    team_group VARCHAR(255),
    team_country_id INT NOT NULL,
    manager_id INT,
    PRIMARY KEY (team_id),
    FOREIGN KEY (team_country_id)
    	REFERENCES Countrys (country_id),
    FOREIGN KEY (manager_id)
    	REFERENCES Managers (manager_id)
);

CREATE TABLE Matches (
    match_id INT UNIQUE,
	competition_id INT NOT NULL,
	season_id INT NOT NULL,
    competition_name VARCHAR(255),
    season_name VARCHAR(255),
    match_date DATE NOT NULL,
    kick_off TIME NOT NULL,
    home_team_id INT NOT NULL,
    away_team_id INT NOT NULL,
    home_score INT NOT NULL,
    away_score INT NOT NULL,
    match_week INT,
    competition_stage VARCHAR(255),
    stadium_id INT,
    referee_id INT,
	PRIMARY KEY (match_id),
	FOREIGN KEY (competition_id)
		REFERENCES Competitions (competition_id),
	FOREIGN KEY (season_id)
		REFERENCES Seasons (season_id),
    FOREIGN KEY (home_team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (away_team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (stadium_id)
    	REFERENCES Stadiums (stadium_id),
    FOREIGN KEY (referee_id)
    	REFERENCES Referees (referee_id)
);

CREATE TABLE Players (
    player_id INT NOT NULL,
    player_name VARCHAR(255) NOT NULL,
    player_nickname VARCHAR(255),
    jersey_number INT,
    country_id INT,
    country_name VARCHAR(255),
    position_id INT,
    position_name VARCHAR(255),
    team_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (player_id),
    FOREIGN KEY (country_name)
    	REFERENCES Countrys (country_name),
    FOREIGN KEY (team_name)
        REFERENCES Teams (team_name)   
);

CREATE TABLE TeamFormations (
    match_id INT,
    team_id INT, 
    formation VARCHAR(255),
    FOREIGN KEY (team_id)
        REFERENCES Teams (team_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id)
);

CREATE TABLE GenericEvents (
    event_id VARCHAR(255) NOT NULL,
    idx INT,
    periods INT,
    time_stamp TIME,
    minute_time INT,
    second_time INT,
    type_id INT,
    type_name VARCHAR(255),
    possession INT,
    possession_team_id INT,
    play_pattern_id INT,
    play_pattern_name VARCHAR(255),
    team_id INT,
    location_x FLOAT,
    location_y FLOAT,
    duration FLOAT,
    counterpress BOOLEAN,
    player_id INT,
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (possession_team_id)
        REFERENCES Teams (team_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE Passes (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    recipient_id INT,
    recipient_name VARCHAR(255),
    pass_length FLOAT,
    angle FLOAT,
    height_id INT,
    height_name VARCHAR(255),
    aerial_won BOOLEAN,
    end_location_x FLOAT,
    end_location_y FLOAT,
    assisted_shot_id VARCHAR(255),
    deflected BOOLEAN,
    miscommunication BOOLEAN,
    is_cross BOOLEAN,
    cut_back BOOLEAN,
    switch BOOLEAN,
    shot_assist BOOLEAN,
    goal_assist BOOLEAN,
    body_part_id INT,
    body_part_name VARCHAR(255),
    pass_type_id INT,
    pass_type_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    technique_id INT,
    technique_name VARCHAR(255),  
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (recipient_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
) PARTITION BY LIST (season_name);


CREATE TABLE Passes_2018_2019_La_Liga_Partition PARTITION OF Passes 
    FOR VALUES IN ('2018/2019');

CREATE TABLE Passes_2019_2020_La_Liga_Partition PARTITION OF Passes 
    FOR VALUES IN ('2019/2020');

CREATE TABLE Passes_2020_2021_La_Liga_Partition PARTITION OF Passes
    FOR VALUES IN ('2020/2021')
    PARTITION BY LIST (technique_name);

-- Create a default partition for all other values
CREATE TABLE Passes_2020_2021_others_La_Liga_Partition PARTITION OF Passes_2020_2021_La_Liga_Partition
    DEFAULT;

CREATE TABLE Through_Balls_2020_2021_La_Liga_Partition PARTITION OF Passes_2020_2021_La_Liga_Partition
    FOR VALUES IN ('Through Ball');

CREATE TABLE Passes_2003_2004_Premier_League_Partition PARTITION OF Passes
    FOR VALUES IN ('2003/2004')
    PARTITION BY LIST (recipient_name);

CREATE TABLE Passes_2003_2004_Premier_League_Partition_Recepient_Partition_Nulls PARTITION OF Passes_2003_2004_Premier_League_Partition
    FOR VALUES IN (NULL);

CREATE TABLE Passes_2003_2004_Premier_League_Partition_Recepient_Partition PARTITION OF Passes_2003_2004_Premier_League_Partition
    DEFAULT;

CREATE INDEX idx_recipient_name ON Passes_2003_2004_Premier_League_Partition_Recepient_Partition(recipient_name);

CREATE TABLE Shots (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    statsbomb_xg FLOAT,
    end_location_x FLOAT,
    end_location_y FLOAT,
    end_location_z FLOAT,
    follows_dribble BOOLEAN,
    first_time BOOLEAN,
    open_goal BOOLEAN,
    deflected BOOLEAN,
    technique_id INT,
    technique_name VARCHAR(255),
    body_part_id INT,
    body_part_name VARCHAR(255),
    type_id INT,
    type_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
        REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
        REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
) PARTITION BY LIST (season_name);

CREATE TABLE ShotsCopy (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    statsbomb_xg FLOAT,
    end_location_x FLOAT,
    end_location_y FLOAT,
    end_location_z FLOAT,
    follows_dribble BOOLEAN,
    first_time BOOLEAN,
    open_goal BOOLEAN,
    deflected BOOLEAN,
    technique_id INT,
    technique_name VARCHAR(255),
    body_part_id INT,
    body_part_name VARCHAR(255),
    type_id INT,
    type_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
        REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
        REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
) PARTITION BY LIST (season_name);

-- Partition 
CREATE TABLE Shots_2018_2019_2020_2021_La_Liga_Partition PARTITION OF Shots 
    FOR VALUES IN ('2018/2019', '2019/2020', '2020/2021')
    PARTITION BY LIST (season_name);

CREATE TABLE Shots_remaining_partition PARTITION OF Shots
    DEFAULT;

CREATE TABLE Shots_2018_2019_2020_2021_La_Liga_Partition_first_time PARTITION OF Shots_2018_2019_2020_2021_La_Liga_Partition 
    FOR VALUES IN ('2018/2019', '2019/2020', '2020/2021')
    PARTITION BY LIST (first_time);

CREATE TABLE Shots_remaining_first_time_La_Liga_Partition PARTITION OF Shots_2018_2019_2020_2021_La_Liga_Partition_first_time
    DEFAULT;

CREATE TABLE First_time_shots_2018_2019_2020_2021_La_Liga_Partition_s PARTITION OF Shots_2018_2019_2020_2021_La_Liga_Partition_first_time
    FOR VALUES IN (True);

CREATE TABLE First_time_shots_2018_2019_2020_2021_La_Liga_Partition_f PARTITION OF Shots_2018_2019_2020_2021_La_Liga_Partition_first_time
    FOR VALUES IN (False);

CREATE TABLE Shots_2018_2019_La_Liga_Partition PARTITION OF ShotsCopy 
    FOR VALUES IN ('2018/2019');

CREATE TABLE Shots_2019_2020_La_Liga_Partition PARTITION OF ShotsCopy 
    FOR VALUES IN ('2019/2020');

CREATE TABLE Shots_2020_2021_La_Liga_Partition PARTITION OF ShotsCopy
    FOR VALUES IN ('2020/2021')
    PARTITION BY RANGE (statsbomb_xg);

CREATE TABLE Shots_2020_2021_La_Liga_Partition_0_1 PARTITION OF Shots_2020_2021_La_Liga_Partition
    FOR VALUES FROM (0) TO (1.000000001); -- will get the statsbomb score values of 0 to 1 is exclusive, what if i want to include 1? I miust use FROM (0) TO (1.000000000001)

CREATE TABLE Shots_2003_2004_Premier_League_Partition PARTITION OF ShotsCopy
    FOR VALUES IN ('2003/2004');

CREATE TABLE Dribbles (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    overrun BOOLEAN,
    nutmeg BOOLEAN,
    outcome_id INT,
    outcome_name VARCHAR(255),
    no_touch BOOLEAN,
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
) PARTITION BY LIST (season_name);

CREATE TABLE Dribbles_2018_2019_2020_2021_La_Liga_Partition PARTITION OF Dribbles
    FOR VALUES IN ('2018/2019', '2019/2020', '2020/2021')
    PARTITION BY LIST (outcome_name);

CREATE TABLE Dribbles_2018_2019_2020_2021_La_Liga_Success_Partition PARTITION OF Dribbles_2018_2019_2020_2021_La_Liga_Partition
    FOR VALUES IN ('Complete');

CREATE TABLE Dribbles_2018_2019_2020_2021_La_Liga_Failure_Partition PARTITION OF Dribbles_2018_2019_2020_2021_La_Liga_Partition
    DEFAULT;

CREATE TABLE Dribbles_2003_2004_Premier_League_Partition PARTITION OF Dribbles
    FOR VALUES IN ('2003/2004');

CREATE TABLE BadBehaviours(
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    card_id INT, 
    card_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE BallReceipts(
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    outcome_id INT,
    outcome_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE BallRecoveries(
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    offensive BOOLEAN,
    recovery_failure BOOLEAN,
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id), 
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE Blocks(
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    deflection BOOLEAN,
    offensive BOOLEAN,
    save_block BOOLEAN,
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE Carries (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    carry_end_location_x FLOAT, 
    carry_end_location_y FLOAT,
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE Clearances (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    aerial_won BOOLEAN,
    body_part_id INT,
    body_part_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE Duels (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    duel_type_id INT,
    duel_type_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE FoulsCommitted (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    offensive BOOLEAN,
    foul_type_id INT,
    foul_type_name VARCHAR(255),
    advantage BOOLEAN,
    penalty BOOLEAN,
    card_id INT,
    card_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE FoulsWon (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    defensive BOOLEAN,
    advantage BOOLEAN,
    penalty BOOLEAN,
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE GoalkeeperEvents (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    position_id INT,
    position_name VARCHAR(255),
    technique_id INT,
    technique_name VARCHAR(255),
    body_part_id INT,
    body_part_name VARCHAR(255),
    type_id INT,
    type_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE Interceptions (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    outcome_id INT,
    outcome_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE Substitutions (
    event_id VARCHAR(255) NOT NULL,
    team_id INT,
    player_id INT,
    replacement_id INT,
    replacement_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE FreezeFrames (
    event_id VARCHAR(255) NOT NULL,
    location_x FLOAT,
    location_y FLOAT,
    player_id INT,
    teammate BOOLEAN,
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
);

CREATE TABLE DribbledPasts ( -- A row for everytime a player is dribbled past --
    event_id VARCHAR(255) NOT NULL,
    player_name VARCHAR(255),
    player_id INT,
    team_name VARCHAR(255),
    match_id INT NOT NULL,
    season_id INT NOT NULL,
    competition_id INT NOT NULL,
    season_name VARCHAR(255) NOT NULL,
    competition_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (event_id)
        REFERENCES GenericEvents (event_id),
    FOREIGN KEY (player_id)
        REFERENCES Players (player_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (season_id)
        REFERENCES Seasons (season_id),
    FOREIGN KEY (competition_id)
        REFERENCES Competitions (competition_id)
) PARTITION BY LIST (season_name);

CREATE TABLE DribbledPasts_2018_2019_La_Liga_Partition PARTITION OF DribbledPasts 
    FOR VALUES IN ('2018/2019') ;

CREATE TABLE DribbledPasts_2019_2020_La_Liga_Partition PARTITION OF DribbledPasts
    FOR VALUES IN ('2019/2020' );

CREATE TABLE DribbledPasts_2020_2021_La_Liga_Partition PARTITION OF DribbledPasts
    FOR VALUES IN ('2020/2021');

CREATE TABLE DribbledPasts_2003_2004_Premier_League_Partition PARTITION OF DribbledPasts
    FOR VALUES IN ('2003/2004');

CREATE TABLE PlayerMinutes (
    player_id INT,
    match_id INT,
    first_half_start_time VARCHAR(255),
    first_half_end_time VARCHAR(255),
    first_half_start_reason VARCHAR(255),
    first_half_end_reason VARCHAR(255),
    second_half_start_time VARCHAR(255),
    second_half_end_time VARCHAR(255),
    second_half_start_reason VARCHAR(255),
    second_half_end_reason VARCHAR(255),
    FOREIGN KEY (player_id)
        REFERENCES Players (player_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id)
);

CREATE TABLE StartingLineups (
    match_id INT,
    team_id INT,
    player_id INT,
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
        REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
        REFERENCES Players (player_id)
);