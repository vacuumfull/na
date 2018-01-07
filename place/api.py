"""Place api."""
from place.models import Place, Comment, Rating, Location


def get_rate_unlogin(place_id: int) -> dict:
    """Get rate for without login user"""
    result = Rating.objects.average_unlogin(place_id)
    return result


def get_rating(place_id: int, user: object) -> dict:
    """Get place rating."""
    result = Rating.objects.average(place_id, user)
    return result


def vote_rating(place_id: int, user: object, vote: int) -> None:
    """Vote for place post."""
    try:
        place = Place.objects.get(pk=place_id)
        Rating.objects.update_or_create(
            place=place, user=user,
            defaults={'value': vote})
    except Place.DoesNotExist:
        pass


def get_comment(place_id: int, offset: int) -> dict:
    """Get place rating."""
    result = Comment.objects.get_last_comments(place_id, int(offset))
    return result


def send_comment(place_id: int, user: object, comment: str) -> None:
    """Add comment for place post."""
    try:
        place = Place.objects.get(pk=place_id)
        Comment.objects.create(place=place, user=user, content=comment)
    except Place.DoesNotExist:
        pass


def list_items(user: object) -> list:
    result = Place.objects.user_items(owner=user)
    return result


def remove_item(item_id:int) -> None:
    try: 
        Place.objects.filter(id=item_id).delete()
    except Place.DoesNotExist:
        pass


def get_locations() -> list:
    """Get place locations"""
    ids = Place.objects.filter(published=True).values_list('id', flat=True)
    locations = Location.objects.filter(place_id__in=ids).values()
    locations_list = [i for i in locations]

    return locations_list
