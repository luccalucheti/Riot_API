from dotenv import load_dotenv
import os
import pygsheets
import requests
import pandas as pd

load_dotenv(override=True)
api_key = os.environ.get('api_key')
service_account = pygsheets.authorize(service_account_file='JSONs/spreadsheet-automator-436913-2e0d40dde567.json')
sheet = service_account.open_by_url('https://docs.google.com/spreadsheets/d/1DVMUAbhfNE6OF3_yydTQnpOPoBGvz6ESliRkIkhVsPU/edit?usp=sharing')

test = sheet.worksheet('title', 'Test')
#print(test.get_as_df())

test_df = test.get_as_df()
test_df['random_numbers'] = 1
#print(test_df)
test.set_dataframe(test_df, 'A1', copy_head=True)

gameName = 'Rhaenyra'
tagLine = '666xx'



def get_puuid(gameName=None, tagLine=None, api_key=None):
    link = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}?api_key={api_key}'
    response = requests.get(link)
    return response.json()['puuid']

get_puuid(gameName, tagLine, api_key)

response = requests.get('https://br1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key=RGAPI-e7880726-61de-41c5-a962-101312488eaa')

print(pd.DataFrame(response.json()['entries']))