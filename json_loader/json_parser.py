# This script will parse the json objects in the events_data, lineups_data, and matches_data directories
# and write the information for each table into a seperate csv file.
from defs import *
from utils import *

def parse_competitions_data():
    dir = './competitions_data/'
    for file_name in os.listdir(dir):
        with open(dir + file_name, encoding='utf-8') as f:
            competitions = json.load(f)
            for competition in competitions:
                if (((competition['season_name'] == '2003/2004' and competition['competition_name'] == 'Premier League') or ((competition['season_name'] == '2018/2019' or competition['season_name'] == '2019/2020' or competition['season_name'] == '2020/2021') and competition['competition_name'] == 'La Liga'))):
                    if not is_existing_id(competitions_arr, competition['competition_id']):
                        competitions_arr.append([competition['competition_id'], competition['competition_name'], competition['country_name'], competition['competition_gender'], competition['competition_youth'], competition['competition_international']])
                    if not is_existing_id(seasons_arr, competition['season_id']):
                        seasons_arr.append([competition['season_id'], competition['competition_id'], competition['season_name']])

def parse_lineups_data():
    dir = './lineups_data/'
    for file_name in os.listdir(dir):
        with open(dir + file_name, encoding='utf-8') as f:
            lineups = json.load(f)
            match_id = file_name.split('.')[0]
            for lineup in lineups: # LOOP THROUGH Each Object in the JSON
                team_name = lineup['team_name']
                for team in lineup['lineup']: # LOOP THROUGH LINEUPS
                    # ---------------Country Array----------------
                    if team.get('country'):
                        country_id = team['country']['id']
                        country_name = team['country']['name']
                        if not is_existing_id(countrys_arr, country_id):
                            countrys_arr.append([country_id, country_name])
                    # --------------------------------------------
                    # ---------------Players and PlayerMinutes Array----------------
                    if team.get('positions'):
                        if len(team['positions']) > 0:
                            first_half_start_time = team['positions'][0]['from']
                            second_half_start_time = team['positions'][-1]['from']
                            first_half_end_time = team['positions'][0]['to']
                            second_half_end_time = team['positions'][-1]['to']
                            first_half_start_reason = team['positions'][0]['start_reason']
                            second_half_start_reason = team['positions'][-1]['start_reason']
                            first_half_end_reason = team['positions'][0]['end_reason']
                            second_half_end_reason = team['positions'][-1]['end_reason']
                        else:
                            first_half_start_time, second_half_start_time, first_half_end_time, second_half_end_time, first_half_start_reason, second_half_start_reason, first_half_end_reason, second_half_end_reason = None, None, None, None, None, None, None, None

                        for position in team['positions']:        

                            if position.get('position_id'): # Set the position to the last position in the list
                                player_position_id = position['position_id'] 
                                player_position_name = position['position']
                            else:
                                player_position_id = None
                                player_position_name = None
                    else:
                        first_half_start_time, second_half_start_time, first_half_end_time, second_half_end_time, first_half_start_reason, second_half_start_reason, first_half_end_reason, second_half_end_reason = None, None, None, None, None, None, None, None
                        player_position_id = None
                        player_position_name = None
                    
                    if not is_existing_id(players_arr, team['player_id']):
                        players_arr.append([team['player_id'], team['player_name'], team['player_nickname'], team['jersey_number'] , team['country']['id'], team['country']['name'], player_position_id, player_position_name, team_name])
                    
                    player_minutes_arr.append([team['player_id'], match_id, first_half_start_time, first_half_end_time, first_half_start_reason, first_half_end_reason, second_half_start_time, second_half_end_time, second_half_start_reason, second_half_end_reason])
                    # --------------------------------------------
            
def parse_matches_data():
    dir = './matches_data/'
    for file_name in os.listdir(dir):
        with open(dir + file_name, encoding='utf-8') as f:
            matches = json.load(f)
            for match in matches:
                stadium_id = None
                if match.get('stadium'):
                    stadium_id = match['stadium']['id']
                    if not is_existing_id(stadiums_arr, match['stadium']['id']):
                        stadiums_arr.append([match['stadium']['id'], match['stadium']['name'], match['stadium']['country']['id']])
                
                referee_id = None
                if match.get('referee'):
                    referee_id = match['referee']['id']
                    if not is_existing_id(referees_arr, match['referee']['id']):
                        referees_arr.append([match['referee']['id'], match['referee']['name'], match['referee']['country']['id']])
                
                matches_arr.append([match['match_id'], match['competition']['competition_id'], match['season']['season_id'], match['competition']['competition_name'], match['season']['season_name'], match['match_date'], match['kick_off'], match['home_team']['home_team_id'], match['away_team']['away_team_id'], match['home_score'], match['away_score'], match['match_week'], match['competition_stage']['name'], stadium_id, referee_id])
                
                if match.get('home_team'):
                    manager_id = None
                    if match['home_team'].get('managers'):
                        manager_id = match['home_team']['managers'][0]['id']
                        for manager in match['home_team']['managers']:
                            if not is_existing_id(managers_arr, manager['id']):
                                managers_arr.append([manager['id'], manager['name'], manager['nickname'], manager['dob'], manager['country']['id']])

                if not is_existing_id(teams_arr, match['home_team']['home_team_id']):
                    teams_arr.append([match['home_team']['home_team_id'], match['home_team']['home_team_name'], match['home_team']['home_team_gender'], match['home_team']['home_team_group'], match['home_team']['country']['id'], manager_id])

                if match.get('away_team'):
                    manager_id_away = None
                    if match['away_team'].get('managers'):
                        manager_id_away = match['away_team']['managers'][0]['id']
                        
                        for manager in match['away_team']['managers']:
                            if not is_existing_id(managers_arr, manager['id']):
                                managers_arr.append([manager['id'], manager['name'], manager['nickname'], manager['dob'], manager['country']['id']])                
                
                if not is_existing_id(teams_arr, match['away_team']['away_team_id']):
                    teams_arr.append([match['away_team']['away_team_id'], match['away_team']['away_team_name'], match['away_team']['away_team_gender'], match['away_team']['away_team_group'], match['away_team']['country']['id'], manager_id_away])



def parse_events_data():
    dir = './events_data/'
    for file_name in os.listdir(dir):
        with open(dir + file_name, encoding='utf-8') as f:
            events = json.load(f)
            match_id = file_name.split('.')[0]
            for event in events:         
                if event.get('tactics'):
                    team_formations_arr.append([match_id, event['team']['id'], event['tactics']['formation']])
                if (event['type']['name'] == 'Starting XI'):
                    for player in event['tactics']['lineup']:
                        starting_lineups_arr.append([match_id, event['team']['id'], player['player']['id']])
                else: # If the event is not the starting XI:
                    # ----- USED BY ALL EVENTS THAT ARE NOT PART OF THE STARTING XI ------------
                    competition_id, season_id, competition_name, season_name = find_matching_competition_and_season(matches_arr, match_id)
                    player_id, player_name = single_attribute_id_name(event, 'player')
                    team_id, team_name = single_attribute_id_name(event, 'team')
                    type_id = event['type']['id']
                    type_name = event['type']['name']
                    event_id = event['id']
                    # ---------------------------------------------------------------------------
                    
                    end_location_x, end_location_y = single_attribute_location_2D(event, 'location')
                    counterpress = single_attribute_info_bool(event, 'counterpress')
                    duration = single_attribute_info(event, 'duration')
                    generic_events_arr.append([event_id, event['index'], event['period'], event['timestamp'], event['minute'], event['second'], type_id, type_name, event['possession'], event['possession_team']['id'], event['play_pattern']['id'], event['play_pattern']['name'], team_id, end_location_x, end_location_y, duration, counterpress, player_id, team_name, player_name, match_id, season_id, competition_id, season_name, competition_name])

                    if (type_name == 'Pass'):
                        recipient_id, recipient_name = nested_attribute_info_id_name(event, 'pass', 'recipient')
                        length = nested_attribute_info(event, 'pass', 'length')
                        angle = nested_attribute_info(event, 'pass', 'angle')
                        height_id, height_name = nested_attribute_info_id_name(event, 'pass', 'height')
                        aerial_won = nested_attribute_info_bool(event, 'pass', 'aerial_won')
                        end_location_x, end_location_y = nested_atrribute_location_2D(event, 'pass', 'end_location')
                        assisted_shot_id = nested_attribute_info(event, 'pass', 'assisted_shot_id')
                        deflected = nested_attribute_info_bool(event, 'pass', 'deflected')
                        miscommunication = nested_attribute_info_bool(event, 'pass', 'miscommunication')
                        is_cross = nested_attribute_info_bool(event, 'pass', 'cross')    
                        cut_back = nested_attribute_info_bool(event, 'pass', 'cut_back')
                        switch = nested_attribute_info_bool(event, 'pass', 'switch')
                        shot_assist = nested_attribute_info_bool(event, 'pass', 'shot_assist')  
                        goal_assist = nested_attribute_info_bool(event, 'pass', 'goal_assist')
                        body_part_id, body_part_name = nested_attribute_info_id_name(event, 'pass', 'body_part')
                        pass_type_id, pass_type_name = nested_attribute_info_id_name(event, 'pass', 'type')
                        outcome_id, outcome_name = nested_attribute_info_id_name(event, 'pass', 'outcome')
                        technique_id, technique_name = nested_attribute_info_id_name(event, 'pass', 'technique') 
                        passes_arr.append([event_id, team_id, player_id, recipient_id, recipient_name, length, angle, height_id, height_name, aerial_won, end_location_x, end_location_y, assisted_shot_id, deflected, miscommunication, is_cross, cut_back, switch, shot_assist, goal_assist, body_part_id, body_part_name, pass_type_id, pass_type_name, outcome_id, outcome_name, technique_id, technique_name, team_name, player_name, match_id, season_id, competition_id, season_name, competition_name])

                    if (type_name == 'Shot'):
                        statsbomb_xg = nested_attribute_info(event, 'shot', 'statsbomb_xg')
                        x, y, z = nested_attribute_location_3D(event, 'shot', 'end_location')
                        follows_dribble = nested_attribute_info_bool(event, 'shot', 'follows_dribble')
                        first_time = nested_attribute_info_bool(event, 'shot', 'first_time')
                        open_goal = nested_attribute_info_bool(event, 'shot', 'open_goal')
                        deflected = nested_attribute_info_bool(event, 'shot', 'deflected')
                        technique_id, technique_name = nested_attribute_info_id_name(event, 'shot', 'technique')
                        body_part_id, body_part_name = nested_attribute_info_id_name(event, 'shot', 'body_part')
                        type_id, type_name = nested_attribute_info_id_name(event, 'shot', 'type')
                        outcome_id, outcome_name = nested_attribute_info_id_name(event, 'shot', 'outcome')
                        shots_arr.append([event_id, team_id, player_id, statsbomb_xg, x, y, z, follows_dribble, first_time, open_goal, deflected, technique_id, technique_name, body_part_id, body_part_name, type_id, type_name, outcome_id, outcome_name, team_name, player_name, match_id, season_id, competition_id, season_name, competition_name])
                        shots_copy_arr.append([event_id, team_id, player_id, statsbomb_xg, x, y, z, follows_dribble, first_time, open_goal, deflected, technique_id, technique_name, body_part_id, body_part_name, type_id, type_name, outcome_id, outcome_name, team_name, player_name, match_id, season_id, competition_id, season_name, competition_name])
                        
                        if (event['shot'].get('freeze_frame')):
                            for freeze_frame in event['shot']['freeze_frame']:
                                freeze_frames_arr.append([event_id, freeze_frame['location'][0], freeze_frame['location'][1], freeze_frame['player']['id'], freeze_frame['teammate'], match_id, season_id, competition_id, season_name, competition_name])
                    
                    if (type_name == 'Dribble'):
                        overrun = nested_attribute_info_bool(event, 'dribble', 'overrun')
                        nutmeg = nested_attribute_info_bool(event, 'dribble', 'nutmeg')
                        no_touch = nested_attribute_info_bool(event, 'dribble', 'no_touch')
                        outcome_id, outcome_name = nested_attribute_info_id_name(event, 'dribble', 'outcome')
                        dribbles_arr.append([event_id, team_id, player_id, overrun, nutmeg, outcome_id, outcome_name, no_touch, team_name, player_name, match_id, season_id, competition_id,season_name, competition_name])

                    if (type_name == 'Bad Behaviour'):
                        card_id, card_name = nested_attribute_info_id_name(event, 'bad_behaviour', 'card')
                        bad_behaviours_arr.append([event_id, team_id, player_id, card_id, card_name, team_name, player_name, match_id, season_id, competition_id, season_name, competition_name])

                    if (type_name == 'Ball Receipt*'):
                        if (event.get('ball_receipt')):
                            outcome_id, outcome_name = nested_attribute_info_id_name(event, 'ball_receipt', 'outcome')
                        else:
                            outcome_id, outcome_name = None, None
                        ball_receipts_arr.append([event['id'], team_id, player_id, outcome_id, outcome_name, team_name, player_name, match_id, season_id, competition_id,season_name, competition_name])

                    if (type_name == 'Ball Recovery'):
                        if (event.get('ball_recovery')):
                            offensive = nested_attribute_info_bool(event, 'ball_recovery', 'offensive')
                            ball_recovery = nested_attribute_info_bool(event, 'ball_recovery', 'recovery_failure')
                        else:
                            offensive, ball_recovery = None, None
                        ball_recoveries_arr.append([event_id, team_id, player_id, offensive, ball_recovery, team_name, player_name, match_id, season_id, competition_id,season_name, competition_name])

                    if (type_name == 'Block'):
                        if (event.get('block')):
                            deflection = nested_attribute_info_bool(event, 'block', 'deflection')   
                            offensive = nested_attribute_info_bool(event, 'block', 'offensive')
                            save_block = nested_attribute_info_bool(event, 'block', 'block')
                        else:
                            deflection, offensive, save_block = None, None, None
                        blocks_arr.append([event_id, team_id, player_id, deflection, offensive, save_block, team_name, player_name, match_id,season_id, competition_id, season_name, competition_name])
                    
                    if (type_name == 'Carry'):
                        x, y = nested_atrribute_location_2D(event, 'carry', 'end_location')
                        carries_arr.append([event_id, team_id, player_id, x, y, team_name, player_name, match_id, season_id, competition_id,season_name, competition_name])

                    if (type_name == 'Clearance'):
                        if (event.get('clearance')):
                            body_part_id, body_part_name = nested_attribute_info_id_name(event, 'clearance', 'body_part')
                            aerail_won = nested_attribute_info_bool(event, 'clearance', 'aerial_won')
                        else:
                            body_part_id, body_part_name, aerail_won = None, None, None 
                        clearances_arr.append([event_id, team_id, player_id, aerail_won, body_part_id, body_part_name, team_name, player_name, match_id,season_id, competition_id, season_name, competition_name])

                    if (type_name == 'Duel'):
                        duel_type_id, duel_type_name = nested_attribute_info_id_name(event, 'duel', 'type')
                        outcome_id, outcome_name = nested_attribute_info_id_name(event, 'duel', 'outcome')
                        duels_arr.append([event_id, team_id, player_id, duel_type_id, duel_type_name, outcome_id, outcome_name, team_name, player_name, match_id,season_id, competition_id, season_name, competition_name])

                    if (type_name == 'Foul Committed'):
                        if (event.get('foul_committed')):
                            offensive = nested_attribute_info_bool(event, 'foul_committed', 'offensive')
                            foul_type_id, foul_type_name = nested_attribute_info_id_name(event, 'foul_committed', 'type')
                            advantage = nested_attribute_info_bool(event, 'foul_committed', 'advantage')    
                            penalty = nested_attribute_info_bool(event, 'foul_committed', 'penalty')    
                            card_id, card_name = nested_attribute_info_id_name(event, 'foul_committed', 'card')
                        else:
                            offensive, foul_type_id, foul_type_name, advantage, penalty, card_id, card_name = None, None, None, None, None, None, None

                        fouls_commited_arr.append([event_id, team_id, player_id, offensive, foul_type_id, foul_type_name, advantage, penalty, card_id, card_name, team_name, player_name, match_id, season_id, competition_id,season_name, competition_name])

                    if (type_name == 'Foul Won'):
                        if (event.get('foul_won')):
                            defensive = nested_attribute_info_bool(event, 'foul_won', 'defensive')
                            advantage = nested_attribute_info_bool(event, 'foul_won', 'advantage')
                            penalty = nested_attribute_info_bool(event, 'foul_won', 'penalty')
                        else:
                            defensive, advantage, penalty = False, False, False
                        fouls_won_arr.append([event_id, team_id, player_id, defensive, advantage, penalty, team_name, player_name, match_id,season_id, competition_id, season_name, competition_name])

                    if (type_name == 'Goal Keeper'):
                        position_id,position_name = nested_attribute_info_id_name(event, 'goalkeeper', 'position')
                        technique_id, technique_name = nested_attribute_info_id_name(event, 'goalkeeper', 'technique')
                        body_part_id, body_part_name = nested_attribute_info_id_name(event, 'goalkeeper', 'body_part')
                        type_id, type_name = nested_attribute_info_id_name(event, 'goalkeeper', 'type')
                        outcome_id, outcome_name = nested_attribute_info_id_name(event, 'goalkeeper', 'outcome')
                        goalkeeper_events_arr.append([event_id, team_id, player_id, position_id, position_name, technique_id, technique_name, body_part_id, body_part_name, type_id, type_name, outcome_id, outcome_name, match_id,season_id, competition_id, season_name, competition_name])

                    if (type_name == 'Interception'):
                        if (event.get('interception')):
                            outcome_id, outcome_name = nested_attribute_info_id_name(event, 'interception', 'outcome')
                        else:
                            outcome_id, outcome_name = None, None
                        interceptions_arr.append([event_id, team_id, player_id, outcome_id, outcome_name, team_name, player_name, match_id, season_id, competition_id,season_name, competition_name])

                    if (type_name == 'Substitution'):
                        replacement_id, replacement_name = nested_attribute_info_id_name(event, 'substitution', 'replacement')
                        outcome_id, outcome_name = nested_attribute_info_id_name(event, 'substitution', 'outcome')
                        subsctitutions_arr.append([event_id, team_id, player_id, replacement_id, replacement_name, outcome_id, outcome_name, team_name, player_name, match_id, season_id, competition_id, season_name, competition_name])

                    if (type_name == 'Dribbled Past'):
                        dribbled_pasts_arr.append([event_id, player_name, player_id, team_name, match_id, season_id, competition_id, season_name, competition_name])

def write_to_csv_records():
    for object in csv_data:
        write_records_to_csv(object['csv_filename'], object['attributes_arr'], object['records_arr'])

def main():
    start_time = time.time()
    parse_competitions_data()
    parse_lineups_data()
    parse_matches_data()
    parse_events_data()
    write_to_csv_records()
    end_time = time.time()
    print("Time taken to parse the json data and write to csv files: ", end_time - start_time, " seconds")
main()