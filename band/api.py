from band.models import Band

def list_items(user: object) -> list:
    result = Band.objects.user_items(owner=user)
    return result


def remove_item(item_id:int) -> None:
    try: 
        Band.objects.filter(id=item_id).delete()
    except Band.DoesNotExist:
        pass