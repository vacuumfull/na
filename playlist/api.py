from playlist.models import Playlist

def list_items(user: object) -> list:
    result = Playlist.objects.user_items(creator=user)
    return result


def remove_item(item_id:int) -> None:
    try: 
        Playlist.objects.filter(id=item_id).delete()
    except Playlist.DoesNotExist:
        pass