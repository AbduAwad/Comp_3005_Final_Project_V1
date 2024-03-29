# PERSONAL PYTHON SCRIPT:
# This file retrieves the data for lineups and events from the github repository
# and stores it localy in this repository. This file is used to load the data
import requests
import json

events_url = 'https://raw.githubusercontent.com/statsbomb/open-data/0067cae166a56aa80b2ef18f61e16158d6a7359a/data/events/'
lineups_url = 'https://raw.githubusercontent.com/statsbomb/open-data/0067cae166a56aa80b2ef18f61e16158d6a7359a/data/lineups/'
extension = '.json'

match_data_file_names = ['2_44', '11_4', '11_42', '11_90']
match_ids = []

# Get the match ids from the match data files, so we can retrieve all events and lineups that have the same match id
def getMatchIDs(): 
    dir = './matches_data/'
    for i in range(len(match_data_file_names)):
        with open(dir + match_data_file_names[i] + extension, encoding='utf-8') as f:
            match_data = json.load(f)
            for match in match_data:
                match_ids.append(match['match_id'])

def getEventsData():
    for i in range(len(match_ids)):
        url = events_url + str(match_ids[i]) + extension
        response = requests.get(url) # get the data from the url
        data = response.json()
        with open('./events_data/' + str(match_ids[i]) + extension, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, indent=4))
            print('Match ID: ' + str(match_ids[i]) + ' events data has been saved')

def getLineupsData():
    for i in range(len(match_ids)):
        url = lineups_url + str(match_ids[i]) + extension
        response = requests.get(url) # get the data from the url
        data = response.json()
        with open('./lineups_data/' + str(match_ids[i]) + extension, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, indent=4))
            print('Match ID: ' + str(match_ids[i]) + ' lineups data has been saved')

def main():
    getMatchIDs()
    getEventsData()
    getLineupsData()

main()