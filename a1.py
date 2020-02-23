import requests
from tqdm import tqdm
import jieba
import IPython
from wordcloud import WordCloud
import os
import time

my_id = '244473233'

# 分析 推塔 杀人的关系

def get_matches(user_id):
	url = 'https://api.opendota.com/api/players/%s/Matches?limit=500&'%(user_id)
	matches = requests.get(url).json()
	match_ids = [match['match_id'] for match in matches]
	return match_ids

def get_match_data(match_id):
	match_url = 'https://api.opendota.com/api/matches/%s'%(match_id)
	match_data = requests.get(match_url).json()
	# if match_data['radiant_win'] == True:
	print(match_data['radiant_score']-match_data['dire_score'],match_data['radiant_win'])
	print(match_data['tower_status_radiant'],match_data['tower_status_dire'])
	print(match_data['duration'])
	return match_data



match_ids = get_matches(my_id)
for match_id in tqdm(match_ids):
	# try:
	get_match_data(match_id)
	# except:
	# 	pass
# get_chat(_id)


# output_cloud(_id)

