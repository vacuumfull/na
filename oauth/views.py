from django.http.response import JsonResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

import requests
import oauth.google
import oauth.vk


def authorize(request, app:str):
	if request.user.is_authenticated:
		raise PermissionDenied()
	return getattr(__load_module(app), 'authorize')(request)

def callback(request, app:str):
	if request.user.is_authenticated:
		raise PermissionDenied()
	getattr(__load_module(app), 'callback')(request)

	return redirect('/')


def __load_module(module_name: str) -> object:
	module = {
		'vk': oauth.vk,
		'google': oauth.google
	}
	return module[module_name]