import os
import csv
import json

def is_existing_id(arr, id):
    for x in range(len(arr)):
        if arr[x][0] == id:
            return True
    return False

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