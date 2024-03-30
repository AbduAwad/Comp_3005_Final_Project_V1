-- DDL --
CREATE TABLE Countrys (
    country_id INT UNIQUE,
    country_name VARCHAR(255) UNIQUE,
    PRIMARY KEY (country_name)
);

CREATE TABLE Competitions (
	competition_id INT UNIQUE,
	competition_name VARCHAR(255) NOT NULL,
    country_name VARCHAR(255) NOT NULL,
    competition_gender VARCHAR(255),
    competition_youth BOOLEAN,
    competition_international BOOLEAN,
	PRIMARY KEY (competition_id),
	FOREIGN KEY (country_name)
    	REFERENCES Country (country_name)
);

CREATE TABLE Seasons (
    season_id INT UNIQUE,
	competition_id INT,
	season_name VARCHAR(255) NOT NULL,
	PRIMARY KEY (season_id),
	FOREIGN KEY (competition_id)
		REFERENCES Competitions (competition_id)
);

CREATE TABLE Stadiums (
    stadium_id INT UNIQUE,
    stadium_name VARCHAR(255) NOT NULL,
    stadium_country_id int NOT NULL,
    FOREIGN KEY (stadium_country_id)
    	REFERENCES Country (country_id)
);

CREATE TABLE Referees (
    referee_id INT UNIQUE,
    referee_name VARCHAR(255) NOT NULL,
    referee_country_id int NOT NULL,
    FOREIGN KEY (referee_country_id)
    	REFERENCES Country (country_id)
);

CREATE TABLE Managers (
    manager_id INT UNIQUE,
    manager_name VARCHAR(255) NOT NULL,
    manager_nickname VARCHAR(255),
    manager_dob DATE,
    manager_country_id int NOT NULL,
    PRIMARY KEY (manager_id),
    FOREIGN KEY (manager_country_id)
    	REFERENCES Country (country_id)
);

CREATE TABLE Teams (
    team_id INT UNIQUE,
    team_name VARCHAR(255) NOT NULL,
    team_gender VARCHAR(255),
    team_group VARCHAR(255),
    team_country_id INT NOT NULL,
    manager_id INT,
    PRIMARY KEY (team_id),
    FOREIGN KEY (team_country_id)
    	REFERENCES Country (country_id),
    FOREIGN KEY (manager_id)
    	REFERENCES Managers (manager_id)
);

CREATE TABLE Matches (
    match_id INT UNIQUE,
	competition_id INT,
	season_id INT,
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
    player_id INT,
    player_name VARCHAR(255) NOT NULL,
    player_nickname VARCHAR(255),
    jersey_number INT,
    country_id INT,
    country_name VARCHAR(255),
    postion_id INT,
    postion_name VARCHAR(255),
    team_name VARCHAR(255)
    PRIMARY KEY(player_id),
    FOREIGN KEY (country_name)
    	REFERENCES Country (country_name),
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
    event_id VARCHAR(255),
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
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (possession_team_id)
        REFERENCES Teams (team_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE Passes (
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    recipient_id INT,
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
    type_id INT,
    type_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    technique_id INT,
    technique_name VARCHAR(255),  
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (recipient_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE Shots(
    event_id VARCHAR(255),
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
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE Dribbles(
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    overrun BOOLEAN,
    nutmeg BOOLEAN,
    outcome_id INT,
    outcome_name VARCHAR(255),
    no_touch BOOLEAN,
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE BadBehaviours(
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    card_id INT, 
    card_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id).
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE BallReceipts(
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    outcome_id INT,
    outcome_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE BallRecoveries(
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    offensive BOOLEAN,
    recovery_failure BOOLEAN,
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE Blocks(
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    deflection BOOLEAN,
    offensive BOOLEAN,
    save_block BOOLEAN,
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE Carries (
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    carry_end_location_x FLOAT, 
    carry_end_location_y FLOAT,
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id)
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name)
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE Clearances (
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    ariel_won BOOLEAN,
    body_part_id INT,
    body_part_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE Duels (
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    type_id INT,
    type_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE FoulsCommitted (
    event_id VARCHAR(255),
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
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE FoulsWon (
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    defensive BOOLEAN,
    advantage BOOLEAN,
    penalty BOOLEAN,
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE GoalkeeperEvents (
    event_id VARCHAR(255),
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
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE Interceptions (
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    outcome_id INT,
    outcome_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE Substitutions (
    event_id VARCHAR(255),
    team_id INT,
    player_id INT,
    replaced_id INT,
    replaced_name VARCHAR(255),
    outcome_id INT,
    outcome_name VARCHAR(255),
    team_name VARCHAR(255),
    player_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (team_id)
    	REFERENCES Teams (team_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE FreezeFrames (
    freeze_frame_id VARCHAR(255),
    location_x FLOAT,
    location_y FLOAT,
    player_id INT,
    teammate BOOLEAN,
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (freeze_frame_id)
    	REFERENCES Shots (event_id),
    FOREIGN KEY (player_id)
    	REFERENCES Players (player_id)
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name)
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE DribbledPasts ( -- A row for everytime a player is dribbled past --
    event_id VARCHAR(255),
    player_name VARCHAR(255),
    player_id INT,
    team_name VARCHAR(255),
    match_id INT,
    season_name VARCHAR(255),
    competition_name VARCHAR(255),
    PRIMARY KEY(event_id),
    FOREIGN KEY (event_id)
        REFERENCES Dribbles (event_id),
    FOREIGN KEY (player_id)
        REFERENCES Players (player_id),
    FOREIGN KEY (match_id)
        REFERENCES Matches (match_id),
    FOREIGN KEY (season_name)
        REFERENCES Seasons (season_name),
    FOREIGN KEY (competition_name)
        REFERENCES Competitions (competition_name)
);

CREATE TABLE PlayerMinutes (
    player_id INT,
    match_id INT,
    first_half_start_time TIME,
    first_half_end_time TIME,
    first_half_start_reason VARCHAR(255),
    first_half_end_reason VARCHAR(255),
    second_half_start_time TIME,
    second_half_end_time TIME,
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