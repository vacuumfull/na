import requests
import json

REDIRECT_URI = 'http://localhost:8000/auth/vk/test'
CLIENT_ID = '6156707'
KEY = 'PQcdbE550phLfARfhfsN'
SERVICE_KEY = '1a2c1bc21a2c1bc21a2c1bc2cf1a71ea6111a2c1a2c1bc240ea0e14d87c7c0cff0aa332'


def get_token():
	uri = f'https://oauth.vk.com/access_token?client_id={CLIENT_ID}&client_secret={KEY}&scope=offline&v=5.74&grant_type=client_credentials'
	resp = requests.get(uri, {})
	print(json.loads(resp.text))
	return json.loads(resp.text)['access_token']

def news_search():
	token = get_token()
	uri = f'https://api.vk.com/method/newsfeed.search?q=techno&start_from=1&count=200&extended=0&access_token={SERVICE_KEY}&v=5.52'
	print(uri)
	resp = requests.get(uri, {})
	return json.loads(resp.text)

def group_search():
	name = 'mosaique.space'
	uri = f'https://api.vk.com/method/groups.getById?group_id={name}&fields=fixed_post&access_token={SERVICE_KEY}&v=5.52'
	resp = requests.get(uri, {})
	result = json.loads(resp.text)
	print(result)
	post_id = '-' + str(result['response'][0]['id']) + '_' + str(result['response'][0]['fixed_post'])
	return get_post(post_id)

def get_post(post_id):
	print(post_id)
	uri = f'https://api.vk.com/method/wall.getById?posts={post_id}&access_token={SERVICE_KEY}&v=5.52'
	resp = requests.get(uri, {})
	return json.loads(resp.text)