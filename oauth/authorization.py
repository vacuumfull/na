from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login

def has_user(username):
	try:
		User.objects.get(username=username)
		return True
	except User.DoesNotExist:
		return False

def prepare_profile(info):
	return {
		'username' : info['profile']['given_name']+ '_' + info['profile']['family_name'],
		'system_id': info['profile']['id'],
		'access_token': info['access_token'],
		'expires_in': info['expires_in']
	}

def creat_and_login(request, profile: dict, Model: object):
	password = User.objects.make_random_password()
	user = User.objects.create_user(username=profile['username'], password=password)
	user.save()
	group = Group.objects.get(name='Пользователи')
	group.user_set.add(user)
	group.save()
	Model.objects.create(
		user=user, 
		system_username=profile['system_username'],
		access_token=profile['access_token']
	)
	user = authenticate(username=profile['username'])
	login(request, user)

def auth(request, profile: dict, Model: object):	
	if has_user(profile['username']) is False:
		creat_and_login(request, profile, Model)
	else:
		try:
			system_name = Model.objects.get(system_id=profile['system_id'])
			Model.objects.filter(system_id=profile['system_id']).update(access_token=profile['access_token'])
			user = authenticate(username=profile['username'])
			login(request, user)
		except system_name.DoesNotExist:
			profile['username'] = '__'.join(profile['username'].split('_'))
			creat_and_login(request, profile, Model)