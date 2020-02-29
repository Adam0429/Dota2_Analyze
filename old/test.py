import requests
from tqdm import tqdm
import jieba
import IPython
from wordcloud import WordCloud
import os
import time

# _id = '158626400' #许b
# _id = '139126387' #炸子
# _id = '241353083' #白逼
_id = '904606353' #我
# _id = '435759920' #田
# _id = '198159239' #机子
# _id = '240110134' #代练
# _id = '143316122' #yidun
# _id = '230767983'

# 分析 推塔 杀人的关系
match_url = 'https://api.opendota.com/api/matches/'

def get_matches(id):
	url = 'https://api.opendota.com/api/players/%s/recentMatches'%(id)
	matches_id = requests.get(url).json
	print(matches_id.text)

def output_cloud(id):
    count = {}
    file = open(id+'_chat.txt','r+')
    chats = file.readlines()
    for chat in chats:
        words = jieba.cut(chat.strip(), cut_all=True)
        for word in words:
            if word not in count.keys():
                count[word] = 1
            else:
                count[word] += 1
    text = '' 
    for key,value in count.items():
        for i in range(value):
            text += key+' '
    wc = WordCloud(
        width=1000,
        height=600,
        font_path='STZHONGS.TTF',
        max_font_size=100,      #字体大小
        min_font_size=30,
        collocations=False, 
        max_words=40 
    )
    wc.generate(text)
    wc.to_file(_id+'.png') #图片保存


def analyze_matchs(id,reverse=False):
    headers = {
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://www.opendota.com/request',
        'Origin': 'https://www.opendota.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }
    matches = requests.get('https://api.opendota.com/api/players/'+id+'/matches').json()
    match_ids = [match['match_id'] for match in matches]
    if reverse:
        match_ids.sort()
    for match_id in tqdm(match_ids):
        response = requests.post('https://api.opendota.com/api/request/'+str(match_id), headers=headers)
        time.sleep(2)

def get_chat(id):
    matches = requests.get('https://api.opendota.com/api/players/'+id+'/matches').json()
    file = open(id+'_chat.txt','w')
    for match in tqdm(matches):
        match_info = requests.get(match_url+str(match['match_id'])).json()
        if 'players' not in match_info.keys():
            continue
        players = match_info['players']
        for player in players:
            if str(player['account_id']) == id:
                if 'player_slot' in player.keys():
                    player_slot = player['player_slot']
                    break
        if 'chat' not in match_info.keys():
            continue
        if match_info['chat'] != None:
            for chat in match_info['chat']:
                if chat['slot'] == player_slot and chat['type'] != 'chatwheel':
                    file.write(chat['key']+'\n')
                    print(chat['key'])

analyze_matchs(_id,reverse=True)
get_matches(_id)
# get_chat(_id)


# output_cloud(_id)

