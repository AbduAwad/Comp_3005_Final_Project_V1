import os
import csv
import json
import time
import psycopg

countrys_arr = []
competitions_arr = []
seasons_arr = []
stadiums_arr = []
referees_arr = []
managers_arr = []
teams_arr = []
matches_arr = []
players_arr = []
team_formations_arr = []
generic_events_arr = []
passes_arr = []
shots_arr = []
dribbles_arr = []
bad_behaviours_arr = []
ball_receipts_arr = []
ball_recoveries_arr = []
blocks_arr = []
carries_arr = []
clearances_arr = []
duels_arr = []
fouls_commited_arr = []
fouls_won_arr = []
goalkeeper_events_arr = []
interceptions_arr = []
subsctitutions_arr = []
freeze_frames_arr = []
dribbled_pasts_arr = []
player_minutes_arr = []
starting_lineups_arr = []
shots_summary_arr = []
stats_bomb_arr = []
first_time_shots_arr = []
player_shots_summary_arr = []
team_passes_summary_arr = []
pass_recipients_arr = []
player_through_balls_arr = []
team_through_balls_arr = []
player_dribbles_arr = []
dribbled_pasts_summary_arr = []

tables = [
    "Countrys", "Competitions", "Seasons", "Stadiums", "Referees", "Managers", 
    "Teams", "Matches", "Players", "TeamFormations", "GenericEvents", "Passes", 
    "Shots", "Dribbles", "BadBehaviours", "BallReceipts", "BallRecoveries", "Blocks", 
    "Carries", "Clearances", "Duels", "FoulsCommitted", "FoulsWon", "GoalkeeperEvents", 
    "Interceptions", "Substitutions", "FreezeFrames", "DribbledPasts", "PlayerMinutes",
    "StartingLineups", "TeamShotsSummary", "Statsbomb", "FirstTimeShots", "PlayerShotsSummary",
    "TeamPassesSummary", "PassRecipients", "PlayerThroughBalls", "TeamThroughBalls", "PlayerDribbles",
    "DribbledPastsSummary"
]

partition_names = [
    'Passes_2020_2021_La_Liga_Partition', 'Passes_remaining_Partition',
    'Pass_recipients_2003_2004_Premier_League_Partition', 'Pass_recipients_remaining_Partition',
    'through_balls_2020_2021_La_Liga_Partition', 'through_balls_remaining_Partition',
    'through_balls_2020_2021_La_Liga_Standard_Partition', 'through_balls_2020_2021_La_Liga_Not_Standard_Partition',
    'through_balls_2020_2021_La_Liga_Partition_team', 'through_balls_remaining_Partition_team',
    'through_balls_2020_2021_La_Liga_Standard_Partition_team', 'through_balls_2020_2021_La_Liga_Not_Standard_Partition_team',
    'Shots_2003_2004_Premier_League_Partition', 'Shots_Remaining_Partition_Team',
    'Shots_2020_2021_La_Liga_Partition_players', 'Shots_remaining_Partition_players',
    'Statsbombxg_2020_2021_La_Liga_Partition', 'Statsbombxg_remaining_La_Liga_Partition',
    'firstime_shots_La_Liga_2018_2019_2020_2021_Partition', 'first_time_shots_remaining_Partition',
    'firstime_shots_La_Liga_2018_2019_2020_2021_True_Partition', 'firstime_shots_La_Liga_2018_2019_2020_2021_False_Partition',
    'Dribbles_2018_2019_2020_2021_La_Liga_Partition', 'Dribbles_2003_2004_Premier_League_Partition',
    'Dribbles_2018_2019_2020_2021_La_Liga_Success_Partition', 'Dribbles_2018_2019_2020_2021_La_Liga_Failure_Partition',
    'DribbledPasts_2020_2021_La_Liga_Partition', 'DribbledPasts_remaining_Partition'
]

DB_index_list = []

csv_filenames = [ 
    "countrys", "competitions", "seasons", "stadiums", "referees", "managers",
    "teams", "matches", "players", "team_formations", "generic_events", "passes",
    "shots", "dribbles", "bad_behaviours", "ball_receipts", "ball_recoveries", "blocks",
    "carries", "clearances", "duels", "fouls_commited", "fouls_won", "goalkeeper_events",
    "interceptions", "subsctitutions", "freeze_frames", "dribbled_pasts", "player_minutes",
    "starting_lineups", "shots_summary", 'stats_bomb_xg', 'first_time_shots', 'player_shots_summary',
    'team_passes_summary', 'pass_recipient_summary', 'player_through_balls_summary', 'team_through_balls_summary',
    'player_dribbles_summary', 'dribbled_pasts_summary'
]

csv_data = [
    {
    'csv_filename': 'csv_records/competitions.csv',
    'attributes_arr': ['competition_id', 'competition_name', 'country_name', 'competition_gender', 'competition_youth', 'competition_international'],
    'records_arr': competitions_arr,
    },
    {
    'csv_filename': 'csv_records/seasons.csv',
    'attributes_arr': ['season_id', 'competition_id', 'season_name'],
    'records_arr': seasons_arr,
    },
    {
    'csv_filename': 'csv_records/countrys.csv',
    'attributes_arr': ['country_id', 'country_name'],
    'records_arr': countrys_arr,
    },
    {
    'csv_filename': 'csv_records/players.csv',
    'attributes_arr': ['player_id', 'player_name', 'player_nickname', 'jersey_number', 'country_id', 'country_name', 'position_id', 'position_name', 'team_name'],
    'records_arr': players_arr,
    },
    {
    'csv_filename': 'csv_records/player_minutes.csv',
    'attributes_arr': ['player_id', 'match_id', 'first_half_start_time', 'first_half_end_time', 'first_half_start_reason', 'first_half_end_reason', 'second_half_start_time', 'second_half_end_time', 'second_half_start_reason', 'second_half_end_reason'],
    'records_arr': player_minutes_arr,
    },
    {
    'csv_filename': 'csv_records/stadiums.csv',
    'attributes_arr': ['stadium_id', 'stadium_name', 'stadium_country_id'],
    'records_arr': stadiums_arr,
    },
    {
    'csv_filename': 'csv_records/referees.csv',
    'attributes_arr': ['referee_id', 'referee_name', 'referee_country_id'],
    'records_arr': referees_arr,
    },
    {
    'csv_filename': 'csv_records/managers.csv',
    'attributes_arr': ['manager_id', 'manager_name', 'manager_nickname', 'manager_dob', 'manager_country_id'],
    'records_arr': managers_arr,
    },
    {
    'csv_filename': 'csv_records/teams.csv',
    'attributes_arr': ['team_id', 'team_name', 'team_gender', 'team_group', 'team_country_id', 'manager_id'],
    'records_arr': teams_arr,
    },
    {
    'csv_filename': 'csv_records/matches.csv',
    'attributes_arr': ['match_id', 'competition_id', 'season_id', 'competition_name', 'season_name', 'match_date', 'kick_off', 'home_team_id', 'away_team_id', 'home_score', 'away_score', 'match_week', 'competition_stage', 'stadium_id', 'referee_id'],
    'records_arr': matches_arr,
    },
    {
    'csv_filename': 'csv_records/team_formations.csv',
    'attributes_arr': ['match_id', 'team_id', 'formation'],
    'records_arr': team_formations_arr,
    },
    {
    'csv_filename': 'csv_records/starting_lineups.csv',
    'attributes_arr': ['match_id', 'team_id', 'player_id'],
    'records_arr': starting_lineups_arr,
    },
    {
    'csv_filename': 'csv_records/generic_events.csv',
    'attributes_arr': ['event_id', 'idx', 'periods', 'time_stamp', 'minute_time', 'second_time', 'type_id', 'type_name', 'possession', 'possession_team_id', 'play_pattern_id', 'play_pattern_name', 'team_id', 'location_x', 'location_y', 'duration', 'counterpress', 'player_id', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id', 'season_name', 'competition_name'],
    'records_arr': generic_events_arr,
    },
    {
    'csv_filename': 'csv_records/passes.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'recipient_id','recipient_name', 'pass_length', 'angle', 'height_id', 'height_name', 'aerial_won', 'end_location_x', 'end_location_y', 'assisted_shot_id', 'deflected', 'miscommunication', 'is_cross', 'cut_back', 'switch', 'shot_assist', 'goal_assist', 'body_part_id', 'body_part_name', 'pass_type_id', 'pass_type_name', 'outcome_id', 'outcome_name', 'technique_id', 'technique_name', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id', 'season_name', 'competition_name'],
    'records_arr': passes_arr,
    },
    {
    'csv_filename': 'csv_records/shots.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'statsbomb_xg', 'end_location_x', 'end_location_y', 'end_location_z', 'follows_dribble', 'first_time', 'open_goal', 'deflected', 'technique_id', 'technique_name', 'body_part_id', 'body_part_name', 'type_id', 'type_name', 'outcome_id', 'outcome_name', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id', 'season_name', 'competition_name'],
    'records_arr': shots_arr,
    },
    {
    'csv_filename': 'csv_records/dribbles.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'overrun', 'nutmeg', 'outcome_id', 'outcome_name', 'no_touch', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id', 'season_name', 'competition_name'],
    'records_arr': dribbles_arr,
    },
    {
    'csv_filename': 'csv_records/bad_behaviours.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'card_id', 'card_name', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id','season_name', 'competition_name'],
    'records_arr': bad_behaviours_arr,
    },
    {
    'csv_filename': 'csv_records/ball_receipts.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'outcome_id', 'outcome_name', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id','season_name', 'competition_name'],
    'records_arr': ball_receipts_arr,
    },
    {
    'csv_filename': 'csv_records/ball_recoveries.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'offensive', 'recovery_failure', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id','season_name', 'competition_name'],
    'records_arr': ball_recoveries_arr,
    },
    {
    'csv_filename': 'csv_records/blocks.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'deflection', 'offensive', 'save_block', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id','season_name', 'competition_name'],
    'records_arr': blocks_arr,
    },
    {
    'csv_filename': 'csv_records/carries.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'carry_end_location_x', 'carry_end_location_y', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id','season_name', 'competition_name'],
    'records_arr': carries_arr,
    },
    {
    'csv_filename': 'csv_records/clearances.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'aerial_won', 'body_part_id', 'body_part_name', 'team_name', 'player_name', 'match_id','season_id', 'competition_id', 'season_name', 'competition_name'],
    'records_arr': clearances_arr,
    },
    {
    'csv_filename': 'csv_records/duels.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'duel_type_id', 'duel_type_name', 'outcome_id', 'outcome_name', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id','season_name', 'competition_name'],
    'records_arr': duels_arr,
    },
    {
    'csv_filename': 'csv_records/fouls_commited.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'offensive', 'foul_type_id', 'foul_type_name', 'advantage', 'penalty', 'card_id', 'card_name', 'team_name', 'player_name', 'match_id','season_id', 'competition_id', 'season_name', 'competition_name'],
    'records_arr': fouls_commited_arr,
    },
    {
    'csv_filename': 'csv_records/fouls_won.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'defensive', 'advantage', 'penalty', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id','season_name', 'competition_name'],
    'records_arr': fouls_won_arr,
    },
    {
    'csv_filename': 'csv_records/goalkeeper_events.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'position_id', 'position_name', 'technique_id', 'technique_name', 'body_part_id', 'body_part_name', 'type_id', 'type_name', 'outcome_id', 'outcome_name', 'match_id', 'season_id', 'competition_id','season_name', 'competition_name'],
    'records_arr': goalkeeper_events_arr,
    },
    {
    'csv_filename': 'csv_records/interceptions.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'outcome_id', 'outcome_name', 'team_name', 'player_name', 'match_id','season_id', 'competition_id', 'season_name', 'competition_name'],
    'records_arr': interceptions_arr,
    },
    {
    'csv_filename': 'csv_records/subsctitutions.csv',
    'attributes_arr': ['event_id', 'team_id', 'player_id', 'replacement_id', 'replacement_name', 'outcome_id', 'outcome_name', 'team_name', 'player_name', 'match_id', 'season_id', 'competition_id','season_name', 'competition_name'],
    'records_arr': subsctitutions_arr,
    },
    {
    'csv_filename': 'csv_records/freeze_frames.csv',
    'attributes_arr': ['event_id', 'location_x', 'location_y', 'player_id', 'teammate', 'match_id','season_id', 'competition_id', 'season_name', 'competition_name'],
    'records_arr': freeze_frames_arr,
    },
    {
    'csv_filename': 'csv_records/dribbled_pasts.csv',
    'attributes_arr': ['event_id', 'player_name', 'player_id', 'team_name','match_id','season_id', 'competition_id', 'season_name', 'competition_name'],
    'records_arr': dribbled_pasts_arr,
    }, 
    {
    'csv_filename': 'csv_records/shots_summary.csv',
    'attributes_arr': ['event_id', 'team_name', 'season_name'],
    'records_arr': shots_summary_arr,
    },
    {
    'csv_filename': 'csv_records/stats_bomb_xg.csv',
    'attributes_arr': ['event_id', 'player_name', 'statsbomb_xg', 'season_name'],
    'records_arr': stats_bomb_arr,
    },
    {
    'csv_filename': 'csv_records/first_time_shots.csv',
    'attributes_arr': ['event_id', 'player_name', 'first_time', 'season_name'],
    'records_arr': first_time_shots_arr,
    },
    {
    'csv_filename': 'csv_records/player_shots_summary.csv',
    'attributes_arr': ['event_id', 'player_name', 'season_name'],
    'records_arr': player_shots_summary_arr,
    },
    {
    'csv_filename': 'csv_records/team_passes_summary.csv',
    'attributes_arr': ['event_id', 'team_name', 'season_name'],
    'records_arr': team_passes_summary_arr,
    },
    {
    'csv_filename': 'csv_records/pass_recipient_summary.csv',
    'attributes_arr': ['event_id', 'recipient_name', 'season_name'],
    'records_arr': pass_recipients_arr,
    },
    {
    'csv_filename': 'csv_records/player_through_balls_summary.csv', 
    'attributes_arr': ['event_id', 'player_name', 'season_name', 'technique_name'],
    'records_arr': player_through_balls_arr,
    },
    {
    'csv_filename': 'csv_records/team_through_balls_summary.csv',
    'attributes_arr': ['event_id', 'team_name', 'season_name', 'technique_name'],
    'records_arr': team_through_balls_arr,
    },
    {
    'csv_filename': 'csv_records/player_dribbles_summary.csv',
    'attributes_arr': ['event_id', 'player_name', 'season_name', 'outcome_name'],
    'records_arr': player_dribbles_arr,
    },
    {
    'csv_filename': 'csv_records/dribbled_pasts_summary.csv',
    'attributes_arr': ['event_id', 'player_name', 'season_name'],
    'records_arr': dribbled_pasts_summary_arr,
    }
]