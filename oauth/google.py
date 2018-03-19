import httplib2
from oauth2client.contrib import gce


def autorize(request):
	print(request)
	credentials = gce.AppAssertionCredentials(scope='https://www.googleapis.com/auth/devstorage.read_write')
	http = credentials.authorize(httplib2.Http())
	print(http)