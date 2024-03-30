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
    if event.get(attribute).get(sub_attribute):
        return event[attribute][sub_attribute][0], event[attribute][sub_attribute][1]
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