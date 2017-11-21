"""Message api."""
from message.models import Message

def send_message(content:str, from_user: object, to_user: object) -> None:
    """Send message to user"""
    try:
        Message.objects.create(content=content, from_user=from_user, to_user=to_user)
    except Message.DoesNotExist:
        pass