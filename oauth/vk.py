from django.shortcuts import redirect
from oauth.authorization import auth
from oauth.models import Vkontakte

import requests
import json

REDIRECT_URI = 'https://nightagenda.ru/auth/vk/callback'
CLIENT_ID = '6156707'
KEY = 'PQcdbE550phLfARfhfsN'
SERVICE_KEY = '1a2c1bc21a2c1bc21a2c1bc2cf1a71ea6111a2c1a2c1bc240ea0e14d87c7c0cff0aa332'
API_URL = 'https://api.vk.com/method/'

def get_username(user_id):
	uri = f'{API_URL}users.get?user_id={str(user_id)}&v=5.52'
	resp = requests.get(uri,{})
	profile = json.loads(resp.text)
	return profile['first_name'] + '_' + profile['last_name']

def authorize(request):
	auth_uri  = f'https://oauth.vk.com/authorize?client_id={CLIENT_ID}&display=page&redirect_uri={REDIRECT_URI}&scope=friends&response_type=code&v=5.74'
	return redirect(auth_uri)

def callback(request):
	access_token = request.GET.get('access_token')
	user_id = request.GET.get('user_id')
	print(user_id)
	username = get_username(str(user_id))
	profile = {
		'username': username,
		'system_id': user_id,
		'access_token': access_token
	}
	auth(request, profile, Vkontakte)