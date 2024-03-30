# This script will parse the json objects in the events_data, lineups_data, and matches_data directories
# and write the information for each table into a seperate csv file.
from utils import *

# competitions_arr = [] -> done
# seasons_arr = [] -> done
# countrys_arr = [] -> done
# players_arr = [] -> done
# player_minutes_arr = [] -> done
# stadiums_arr = [] -> done
# referees_arr = [] -> done
# managers_arr = [] -> done
# teams_arr = [] -> done
# matches_arr = [] -> done

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
                
                matches_arr.append([match['match_id'], match['competition']['competition_id'], match['season']['season_id'], match['match_date'], match['kick_off'], match['home_team']['home_team_id'], match['away_team']['away_team_id'], match['home_score'], match['away_score'], match['match_week'], match['competition_stage']['name'], stadium_id, referee_id])
                
                if match.get('home_team'):
                    manager_id = None
                    if match['home_team'].get('managers'):
                        manager_id = match['home_team']['managers'][0]['id']
                        for manager in match['home_team']['managers']:
                            if not is_existing_id(managers_arr, manager['id']):
                                managers_arr.append([manager['id'], manager['name'], manager['nickname'], manager['dob'], manager['country']['id']])

                if not is_existing_id(teams_arr, match['home_team']['home_team_id']):
                            teams_arr.append([match['match_id'], match['competition']['competition_id'], match['season']['season_id'], match['match_date'], match['kick_off'], match['home_team']['home_team_id'], match['away_team']['away_team_id'], match['home_score'], match['away_score'], match['match_week'], match['competition_stage']['name'], manager_id])

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
    print("COMPLETE...")

def write_to_csv_records():

    with open('csv_records/competitions.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['competition_id', 'competition_name', 'country_name', 'competition_gender', 'competition_youth', 'competition_international'])
        for i in range(len(competitions_arr)):
            writer.writerow([competitions_arr[i][0], competitions_arr[i][1], competitions_arr[i][2], competitions_arr[i][3], competitions_arr[i][4], competitions_arr[i][5]])

    with open('csv_records/seasons.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['season_id', 'competition_id', 'season_name'])
        for i in range(len(seasons_arr)):
            writer.writerow([seasons_arr[i][0], seasons_arr[i][1], seasons_arr[i][2]])

    with open('csv_records/countrys.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['country_id', 'country_name'])
        for i in range(len(countrys_arr)):
            writer.writerow([countrys_arr[i][0], countrys_arr[i][1]])

    with open('csv_records/players.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['player_id', 'player_name', 'player_nickname', 'jersey_number', 'country_id', 'country_name', 'position_id', 'position_name', 'team_name'])
        for i in range(len(players_arr)):
            writer.writerow([players_arr[i][0], players_arr[i][1], players_arr[i][2], players_arr[i][3], players_arr[i][4], players_arr[i][5], players_arr[i][6], players_arr[i][7], players_arr[i][8]])

    with open('csv_records/player_minutes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['player_id', 'match_id', 'first_half_start_time', 'first_half_end_time', 'first_half_start_reason', 'first_half_end_reason', 'second_half_start_time', 'second_half_end_time', 'second_half_start_reason', 'second_half_end_reason'])
        for i in range(len(player_minutes_arr)):
            writer.writerow([player_minutes_arr[i][0], player_minutes_arr[i][1], player_minutes_arr[i][2], player_minutes_arr[i][3], player_minutes_arr[i][4], player_minutes_arr[i][5], player_minutes_arr[i][6], player_minutes_arr[i][7], player_minutes_arr[i][8], player_minutes_arr[i][9]])

    with open('csv_records/stadiums.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['stadium_id', 'stadium_name', 'stadium_country_id'])
        for i in range(len(stadiums_arr)):
            writer.writerow([stadiums_arr[i][0], stadiums_arr[i][1], stadiums_arr[i][2]])
        
    with open('csv_records/referees.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['referee_id', 'referee_name', 'referee_country_id'])
        for i in range(len(referees_arr)):
            writer.writerow([referees_arr[i][0], referees_arr[i][1], referees_arr[i][2]])

    with open('csv_records/managers.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['manager_id', 'manager_name', 'manager_nickname', 'dob', 'country_id'])
        for i in range(len(managers_arr)):
            writer.writerow([managers_arr[i][0], managers_arr[i][1], managers_arr[i][2], managers_arr[i][3], managers_arr[i][4]])

    with open('csv_records/teams.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['team_id', 'team_name', 'team_gender', 'team_group', 'country_id', 'manager_id'])
        for i in range(len(teams_arr)):
            writer.writerow([teams_arr[i][0], teams_arr[i][1], teams_arr[i][2], teams_arr[i][3], teams_arr[i][4], teams_arr[i][5]])

    with open('csv_records/matches.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['match_id', 'competition_id', 'season_id', 'match_date', 'kick_off', 'home_team_id', 'away_team_id', 'home_score', 'away_score', 'match_week', 'competition_stage_name', 'stadium_id', 'referee_id'])
        for i in range(len(matches_arr)):
            writer.writerow([matches_arr[i][0], matches_arr[i][1], matches_arr[i][2], matches_arr[i][3], matches_arr[i][4], matches_arr[i][5], matches_arr[i][6], matches_arr[i][7], matches_arr[i][8], matches_arr[i][9], matches_arr[i][10], matches_arr[i][11], matches_arr[i][12]]) 

def main():
    parse_competitions_data()
    parse_lineups_data()
    parse_matches_data()
    parse_events_data()
    write_to_csv_records()
main()