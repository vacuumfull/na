import httplib2
from django.shortcuts import redirect
from oauth2client.contrib import gce
from oauth2client.client import flow_from_clientsecrets


def autorize(request):
	print(request)
	credentials = gce.AppAssertionCredentials(scope='https://www.googleapis.com/auth/devstorage.read_write')
	http = credentials.authorize(httplib2.Http())
	print(http)

def testcallback(request):
	flow = flow_from_clientsecrets('oauth/secret.json',
                               scope='https://www.googleapis.com/auth/calendar',
                               redirect_uri='http://nightagenda.ru/auth/testoauth')
	auth_uri = flow.step1_get_authorize_url()
	return redirect(auth_uri)