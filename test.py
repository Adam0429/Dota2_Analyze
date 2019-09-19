import requests
from tqdm import tqdm
import IPython


import requests

headers = {
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://www.opendota.com/request',
    'Origin': 'https://www.opendota.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}


# _id = '158626400' #许b
# _id = '139126387' #炸子
_id = '241353083' #白逼
# _id = '904606353' #我

url = 'https://api.opendota.com/api/matches/'
matches = requests.get('https://api.opendota.com/api/players/'+_id+'/matches').json()
for match in tqdm(matches):
    response = requests.post('https://api.opendota.com/api/request/'+str(match['match_id']), headers=headers)
    print(response.text)

    # match_info = requests.get(url+str(match['match_id'])).json()
    # if 'players' not in match_info.keys():
    #     continue
    # players = match_info['players']
    # for player in players:
    #     if str(player['account_id']) == _id:
    #         if 'player_slot' in player.keys():
    #             player_slot = player['player_slot']
    #             break
    # if 'chat' not in match_info.keys():
    #     continue
    # if match_info['chat'] != None:
    #     for chat in match_info['chat']:
    #         if chat['slot'] == player_slot and chat['type'] != 'chatwheel':
    #             print(chat['key'])
    #     # IPython.embed()

