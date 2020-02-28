import requests
from tqdm import tqdm
import IPython
from wordcloud import WordCloud
import csv
import pandas as pd 

# 分析 推塔 杀人的关系
def alive_towers(n):
	return str(bin(n))[2:].count('1')

def getMatchId(user_id,number):
	url = 'https://api.opendota.com/api/players/%s/Matches?limit=%s'%(user_id,str(number))
	matches = requests.get(url).json()
	match_ids = [match['match_id'] for match in matches]
	return match_ids

def getMatchData(match_id):
	match_url = 'https://api.opendota.com/api/matches/%s'%(match_id)
	match_data = requests.get(match_url).json()
	# if match_data['radiant_win'] == True:
	# print(match_data['radiant_score']-match_data['dire_score'],match_data['radiant_win'])
	# print(alive_towers(match_data['tower_status_radiant']),alive_towers(match_data['tower_status_dire']))
	# print(match_data['duration'])
	return match_data


my_id = '904606353' #我

match_ids = getMatchId(my_id,1400)
raw_data = []
for match_id in tqdm(match_ids):
	raw_data.append(getMatchData(match_id))
IPython.embed()
df = pd.DataFrame(raw_data,index=None)
df.to_csv('raw_data.csv')
# except:
	# 	pass
# get_chat(_id)


# output_cloud(_id)

