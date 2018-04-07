from django.shortcuts import redirect
from oauth2client.contrib import gce
from oauth2client.client import flow_from_clientsecrets, OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth.authorization import auth, prepare_profile
from oauth.models import Google

import requests
import json

flow = flow_from_clientsecrets('oauth/secret.json',
                               scope='https://www.googleapis.com/auth/plus.login',
                               redirect_uri='http://localhost:8000/auth/google/callback')

def get_profile(credentials, request):
	url = f'https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={credentials.access_token}'
	resp = requests.get(url, {})
	return {
		'profile': json.loads(resp.text),
		'access_token': credentials.access_token,
		'expires_in': credentials.token_expiry
	}

def authorize(request):
	auth_uri = flow.step1_get_authorize_url()
	return redirect(auth_uri)
	

def callback(request):
	code = request.GET.get('code')
	credentials = flow.step2_exchange(code)
	profile = prepare_profile(get_profile(credentials,request))
	auth(request, profile, Google)
