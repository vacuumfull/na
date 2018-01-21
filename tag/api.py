from collections import Counter

from band.models import Band
from blog.models import Blog
from event.models import Event
from place.models import Place
from playlist.models import Playlist



def search_in_blogs(keyword:str) -> list:
	try:
		blogs = Blog.objects.filter(tags__name__in=[keyword], published=True).distinct().values('title', 'annotation', 'content', 'image',
																'slug', 'rubric','author__username', 
																'event__title', 'place__title')
		blog_list = [x for x in blogs]
		return blog_list

	except Blog.DoesNotExist:
		pass

def search_in_events(keyword:str):
	try:
		events = Event.objects.filter(tags__name__in=[keyword], published=True).distinct().values('title', 'description', 'image', 'date', 'price', 'slug', 'owner__username')
		event_list = [x for x in events]
		return event_list
	except Event.DoesNotExist:
		pass

def search_in_places(keyword:str):
	try:
		places = Place.objects.filter(tags__name__in=[keyword], published=True).distinct().values('title', 'description', 'image', 'slug', 'owner__username')
		places_list = [x for x in places]
		return places_list
	except Place.DoesNotExist:
		pass

def search_in_bands(keyword:str):
	try:
		bands = Band.objects.filter(tags__name__in=[keyword], published=True).distinct().values('name', 'description', 'image', 'slug', 'owner__username')
		bands_list = [x for x in bands]
		return bands_list
	except Band.DoesNotExist:
		pass

def search_in_playlists(keyword:str):
	try:
		playlists = Playlist.objects.filter(tags__name__in=[keyword], published=True).distinct().values('name', 'annotation', 'content', 'image', 'slug', 'creator__username')
		playlists_list = [x for x in playlists]
		return playlists_list
	except Playlist.DoesNotExist:
		pass


def fast_search_tags(keyword:str):
	return []

def count_tags() -> list:

	band_tags = Band.tags.values('name')[:20]
	blog_tags = Blog.tags.values('name')[:20]
	event_tags = Event.tags.values('name')[:20]
	place_tags = Place.tags.values('name')[:20]
	playlist_tags = Playlist.tags.values('name')[:20]

	tags = []
	
	all_list = [x for x in band_tags] +  [x for x in blog_tags] + [x for x in event_tags] + [x for x in place_tags] + [x for x in playlist_tags]

	for item in all_list: tags.append(item['name'].lower())

	return Counter(tags)