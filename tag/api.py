from tag.models import Tag


def fast_search_tags(keyword:str) -> list:
    try: 
        tags = Tag.objects.filter(name__contains=keyword).values('name')[:30]
        tags_list = [x for x in tags]
        return tags_list
    except Tag.DoesNotExist:
        pass


def search_in_blogs(keyword:str) -> list:
    try:
        tag = Tag.objects.filter(name=keyword).first()
        blogs = tag.blog_tags.filter(published=True).values('title', 'annotation', 'content', 'image',
                                                            'slug', 'rubric','author__username', 
                                                            'event__title', 'place__title')
        blog_list = [x for x in blogs]
        return blog_list

    except Tag.DoesNotExist:
        pass


def search_in_events(keyword:str) -> list:
    try:
        tag = Tag.objects.filter(name=keyword).first()
        events = tag.event_tags.filter(published=True).values('title', 'description', 'image', 'date', 'price', 'slug', 'owner__username')
        event_list = [x for x in events]
        return event_list

    except Tag.DoesNotExist:
        pass


def search_in_places(keyword:str) -> list:
    try:
        tag = Tag.objects.filter(name=keyword).first()
        places = tag.place_tags.filter(published=True).values('title', 'description', 'image', 'slug', 'owner__username')
        place_list = [x for x in places]
        return place_list

    except Tag.DoesNotExist:
        pass


def search_in_bands(keyword:str) -> list:
    try:
        tag = Tag.objects.filter(name=keyword).first()
        bands = tag.band_tags.filter(published=True).values('name', 'description', 'image', 'slug', 'owner__username')
        band_list = [x for x in bands]
        return band_list

    except Tag.DoesNotExist:
        pass


def count_tags() -> list:
    try:
        tags = Tag.objects.all()[:30]
        counted_list = []
        for tag in tags:
            tag_count = tag.blog_tags.count() + tag.event_tags.count() + tag.place_tags.count() + tag.band_tags.count()
            counted_list.append({'name': tag.name, 'count': tag_count})
       
        return sorted(counted_list, key=lambda d: d['count'], reverse=True)

    except Tag.DoesNotExist:
        pass
