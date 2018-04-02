from django.http.response import JsonResponse
from django.shortcuts import redirect
from oauth2client.contrib import gce
from oauth2client.client import flow_from_clientsecrets, OAuth2WebServerFlow
from oauth2client.file import Storage
from googleapiclient.discovery import build

import requests
import httplib2
import pickle
import json

storage = Storage('a_credentials_file')
flow = flow_from_clientsecrets('oauth/secret.json',
                               scope='https://www.googleapis.com/auth/plus.login',
                               redirect_uri='http://localhost:8000/auth/google/callback')

def test(request):
	credentials = storage.get()
	url = f'https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={credentials.access_token}'
	resp = requests.get(url, {})

	return JsonResponse({'response': json.loads(resp.text)}, safe=False)

def autorize(request):
	auth_uri = flow.step1_get_authorize_url()
	return redirect(auth_uri)
	

def callback(request):
	code = request.GET.get('code')
	credentials = flow.step2_exchange(code)
	
	storage.put(credentials)
	return JsonResponse({'response': 'success'})
	