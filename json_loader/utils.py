import os
import csv
import json

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

competitions_arr_names = ['competition_id', 'competition_name', 'country_name', 'competition_gender', 'competition_youth', 'competition_international']
seasons_arr_names = ['season_id', 'competition_id', 'season_name']
countrys_arr_names = ['country_id', 'country_name']
players_arr_names = ['player_id', 'player_name', 'player_nickname', 'jersey_number', 'country_id', 'country_name', 'position_id', 'position_name', 'team_name']
player_minutes_arr_names = ['player_id', 'match_id', 'first_half_start_time', 'first_half_end_time', 'first_half_start_reason', 'first_half_end_reason', 'second_half_start_time', 'second_half_end_time', 'second_half_start_reason', 'second_half_end_reason']
stadiums_arr_names = ['stadium_id', 'stadium_name', 'stadium_country_id']
referees_arr_names = ['referee_id', 'referee_name', 'referee_country_id']
managers_arr_names = ['manager_id', 'manager_name', 'manager_nickname', 'dob', 'country_id']
teams_arr_names = ['team_id', 'team_name', 'team_gender', 'team_group', 'country_id', 'manager_id']
matches_arr_names = ['match_id', 'competition_id', 'season_id', 'competition_name', 'season_name', 'match_date', 'kick_off', 'home_team_id', 'away_team_id', 'home_score', 'away_score', 'match_week', 'competition_stage_name', 'stadium_id', 'referee_id']
team_formations_arr_names = ['match_id', 'team_id', 'formation']
starting_lineups_arr_names = ['match_id', 'team_id', 'player_id']
generic_events_arr_names = ['event_id', 'index', 'period', 'timestamp', 'minute', 'second', 'type_id', 'type_name', 'possession', 'possession_team_id', 'play_pattern_id', 'play_pattern_name', 'team_id', 'location_x', 'location_y', 'duration', 'counterpress', 'player_id', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
passes_arr_names = ['event_id', 'team_id', 'player_id', 'recipient_id', 'length', 'angle', 'height_id', 'height_name', 'aerial_won', 'end_location_x', 'end_location_y', 'assisted_shot_id', 'deflected', 'miscommunication', 'is_cross', 'cut_back', 'switch', 'shot_assist', 'goal_assist', 'body_part_id', 'body_part_name', 'pass_type_id', 'pass_type_name', 'outcome_id', 'outcome_name', 'technique_id', 'technique_name', 'match_id', 'season_name', 'competition_name']
shots_arr_names = ['event_id', 'team_id', 'player_id', 'statsbomb_xg', 'x', 'y', 'z', 'follows_dribble', 'first_time', 'open_goal', 'deflected', 'technique_id', 'technique_name', 'body_part_id', 'body_part_name', 'type_id', 'type_name', 'outcome_id', 'outcome_name', 'match_id', 'season_name', 'competition_name']
dribbles_arr_names = ['event_id', 'team_id', 'player_id', 'overrun', 'nutmeg', 'outcome_id', 'outcome_name', 'no touch', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
bad_behaviours_arr_names = ['event_id', 'team_id', 'player_id', 'card_id', 'card_name', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
ball_receipts_arr_names = ['event_id', 'team_id', 'player_id', 'outcome_id', 'outcome_name', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
ball_recoveries_arr_names = ['event_id', 'team_id', 'player_id', 'offensive', 'ball_recovery', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
blocks_arr_names = ['event_id', 'team_id', 'player_id', 'deflection', 'offensive', 'save_block', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
carries_arr_names = ['event_id', 'team_id', 'player_id', 'end_location_x', 'end_location_y', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
clearances_arr_names = ['event_id', 'team_id', 'player_id', 'aerial_won', 'body_part_id', 'body_part_name', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
duels_arr_names = ['event_id', 'team_id', 'player_id', 'duel_type_id', 'duel_type_name', 'outcome_id', 'outcome_name', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
fouls_commited_arr_names = ['event_id', 'team_id', 'player_id', 'offensive', 'foul_type_id', 'foul_type_name', 'advantage', 'penalty', 'card_id', 'card_name', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
fouls_won_arr_names = ['event_id', 'team_id', 'player_id', 'defensive', 'advantage', 'penalty', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
goalkeeper_events_arr_names = ['event_id', 'team_id', 'player_id', 'position_id', 'position_name', 'technique_id', 'technique_name', 'body_part_id', 'body_part_name', 'type_id', 'type_name', 'outcome_id', 'outcome_name', 'match_id', 'season_name', 'competition_name']
interceptions_arr_names = ['event_id', 'team_id', 'player_id', 'outcome_id', 'outcome_name', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
subsctitutions_arr_names = ['event_id', 'team_id', 'player_id', 'replacement_id', 'replacement_name', 'outcome_id', 'outcome_name', 'team_name', 'player_name', 'match_id', 'season_name', 'competition_name']
freeze_frames_arr_names = ['event_id', 'location_x', 'location_y', 'player_id', 'teammate', 'match_id', 'season_name', 'competition_name']
dribbled_pasts_arr_names = ['event_id', 'player_name', 'player_id', 'team_name', 'match_id', 'season_name', 'competition_name']

csv_names_arr = [
    countrys_arr_names, competitions_arr_names, seasons_arr_names, stadiums_arr_names, referees_arr_names, managers_arr_names,
    teams_arr_names, matches_arr_names, players_arr_names, team_formations_arr_names, generic_events_arr_names, passes_arr_names,
    shots_arr_names, dribbles_arr_names, bad_behaviours_arr_names, ball_receipts_arr_names, ball_recoveries_arr_names, blocks_arr_names,
    carries_arr_names, clearances_arr_names, duels_arr_names, fouls_commited_arr_names, fouls_won_arr_names, goalkeeper_events_arr_names,
    interceptions_arr_names, subsctitutions_arr_names, freeze_frames_arr_names, dribbled_pasts_arr_names, player_minutes_arr_names,
    starting_lineups_arr_names
]

# Put all csv filenames into sepereate strings
competitions_csv = 'csv_records/competitions.csv'
seasons_csv = 'csv_records/seasons.csv'
countrys_csv = 'csv_records/countrys.csv'
players_csv = 'csv_records/players.csv'
player_minutes_csv = 'csv_records/player_minutes.csv'
stadiums_csv = 'csv_records/stadiums.csv'
referees_csv = 'csv_records/referees.csv'
managers_csv = 'csv_records/managers.csv'
teams_csv = 'csv_records/teams.csv'
matches_csv = 'csv_records/matches.csv'
team_formations_csv = 'csv_records/team_formations.csv'
starting_lineups_csv = 'csv_records/starting_lineups.csv'
generic_events_csv = 'csv_records/generic_events.csv'
passes_csv = 'csv_records/passes.csv'
shots_csv = 'csv_records/shots.csv'
dribbles_csv = 'csv_records/dribbles.csv'
bad_behaviours_csv = 'csv_records/bad_behaviours.csv'
ball_receipts_csv = 'csv_records/ball_receipts.csv'
ball_recoveries_csv = 'csv_records/ball_recoveries.csv'
blocks_csv = 'csv_records/blocks.csv'
carries_csv = 'csv_records/carries.csv'
clearances_csv = 'csv_records/clearances.csv'
duels_csv = 'csv_records/duels.csv'
fouls_commited_csv = 'csv_records/fouls_commited.csv'
fouls_won_csv = 'csv_records/fouls_won.csv'
goalkeeper_events_csv = 'csv_records/goalkeeper_events.csv'
interceptions_csv = 'csv_records/interceptions.csv'
subsctitutions_csv = 'csv_records/subsctitutions.csv'
freeze_frames_csv = 'csv_records/freeze_frames.csv'
dribbled_pasts_csv = 'csv_records/dribbled_pasts.csv'

# Same order as the strings
csv_files_arr = [
    countrys_csv, competitions_csv, seasons_csv, stadiums_csv, referees_csv, managers_csv,
    teams_csv, matches_csv, players_csv, team_formations_csv, generic_events_csv, passes_csv,
    shots_csv, dribbles_csv, bad_behaviours_csv, ball_receipts_csv, ball_recoveries_csv, blocks_csv,
    carries_csv, clearances_csv, duels_csv, fouls_commited_csv, fouls_won_csv, goalkeeper_events_csv,
    interceptions_csv, subsctitutions_csv, freeze_frames_csv, dribbled_pasts_csv, player_minutes_csv,
    starting_lineups_csv
]

def is_existing_id(arr: list, id: int) -> bool:
    for x in range(len(arr)):
        if arr[x][0] == id:
            return True
    return False

def find_matching_competition_and_season(matches_arr: list, match_id: int) -> tuple[int, int]:
    for match in matches_arr:
        if str(match[0]) == match_id:
            return match[3], match[4]
    return None, None

def single_attribute_info(event: dict, attribute: str) -> str:
    if event.get(attribute):    
        attribute = event[attribute]
    else:
        attribute = None
    return attribute

def single_attribute_info_bool(event: dict, attribute: str) -> bool:
    if event.get(attribute):    
        attribute = event[attribute]
    else:
        attribute = False
    return attribute

def single_attribute_id_name(event: dict, attribute: str) -> tuple[int, str]:
    if event.get(attribute):
        return event[attribute]['id'], event[attribute]['name']
    else:
        return None, None
def nested_attribute_info(event: dict, attribute: str, sub_attribute: str) -> str:
    if event.get(attribute).get(sub_attribute):
        return event[attribute][sub_attribute]
    else:
        return None
    
def nested_attribute_info_bool(event: dict, attribute: str, sub_attribute:str) -> bool:
    if event.get(attribute).get(sub_attribute):
        return event[attribute][sub_attribute]
    else:
        return False

def nested_attribute_info_id(event: dict, attribute: str, sub_attribute: str) -> int:
    if event.get(attribute).get(sub_attribute):
        return event[attribute][sub_attribute]['id']
    else:
        return None
    
def nested_attribute_info_id_name(event: dict, attribute: str, sub_attribute: str) -> tuple[int, str]:
    if event.get(attribute).get(sub_attribute):
        return event[attribute][sub_attribute]['id'], event[attribute][sub_attribute]['name']
    else:
        return None, None

def single_attribute_location_2D(event: dict, attribute: str) -> tuple[float, float]:
    if event.get(attribute):
        return event[attribute][0], event[attribute][1]
    else:
        return None, None
    
def nested_atrribute_location_2D(event: dict, attribute: str, sub_attribute: str) -> tuple[float, float]:
    if event.get(attribute):
        if event.get(attribute).get(sub_attribute):
            return event[attribute][sub_attribute][0], event[attribute][sub_attribute][1]
        else:
            return None, None
    else:
        return None, None
        
def nested_attribute_location_3D(event: dict, attribute: str, sub_attribute: str) -> tuple[float, float, float]:
    if event.get(attribute).get(sub_attribute):
        x = event[attribute][sub_attribute][0]
        y = event[attribute][sub_attribute][1]
        if len(event[attribute][sub_attribute]) > 2:
            z = event[attribute][sub_attribute][2]
        else:
            z = None
    else:
        x, y, z = None, None, None
    return x, y, z

def write_records_to_csv(file_name: str, names_arr: list, values_arr: list):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(names_arr)
        for i in range(len(values_arr)):
            row_arr = []
            for x in range(len(values_arr[i])):
                row_arr.append(values_arr[i][x])
            writer.writerow(row_arr)