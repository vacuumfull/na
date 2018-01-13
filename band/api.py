from band.models import Band, Comment

def list_items(user: object) -> list:
    result = Band.objects.user_items(owner=user)
    return result


def remove_item(item_id:int) -> None:
    try: 
        Band.objects.filter(id=item_id).delete()
    except Band.DoesNotExist:
        pass


def get_comment(band_id: int, offset: int) -> dict:
    """Get band comments."""
    result = Comment.objects.get_last_comments(band_id, int(offset))
    return result


def send_comment(band_id: int, user: object, comment: str) -> None:
    """Add comment for band post."""
    try:
        band = Band.objects.get(pk=band_id)
        Comment.objects.create(band=band, user=user, content=comment)
    except Band.DoesNotExist:
        pass