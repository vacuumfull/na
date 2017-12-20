"""Event api."""
from event.models import Event, Comment, Rating


def get_rate_unlogin(event_id: int) -> dict:
    """Get rate for without login user"""
    result = Rating.objects.average_unlogin(event_id)
    return result


def get_rating(event_id: int, user: object) -> dict:
    """Get blog rating."""
    result = Rating.objects.average(event_id, user)
    return result


def vote_rating(event_id: int, user: object, vote: int) -> None:
    """Vote for blog post."""
    try:
        blog = Event.objects.get(pk=event_id)
        Rating.objects.update_or_create(
            blog=blog, user=user,
            defaults={'value': vote})
    except Event.DoesNotExist:
        pass


def get_comment(event_id: int, offset: int) -> dict:
    """Get blog rating."""
    result = Comment.objects.get_last_comments(event_id, int(offset))
    return result


def send_comment(event_id: int, user: object, comment: str) -> None:
    """Add comment for blog post."""
    try:
        blog = Event.objects.get(pk=event_id)
        Comment.objects.create(blog=blog, user=user, content=comment)
    except Event.DoesNotExist:
        pass
