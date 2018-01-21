from member.models import UserSettings, UserExtend
import json

def get_settings(user:object) -> dict:
	"""Get all user settings"""
	settings = UserSettings.objects.filter(user=user).values()
	extend = UserExtend.objects.filter(user=user).values()
	settings_list = [i for i in settings]
	extend_list = [i for i in extend]
	result = {'settings': settings_list, 'extend': extend_list}
	
	return result


def update_settings(user:object, params:dict) -> None:
	"""Update only setting values"""
	try:
		UserSettings.objects.filter(user=user).update(
			alert_comment=params['comment'],
			alert_blog=params['blog'],
			alert_rating=params['rating'],
			alert_link=params['link']
			) 
     
	except UserSettings.DoesNotExist:
		pass


def update_prefer_styles(user:object, styles:list) -> None:
	music = json.dumps(styles)
	try:
		UserExtend.objects.filter(user=user).update(prefer_styles=music)
	except UserExtend.DoesNotExist:
		pass