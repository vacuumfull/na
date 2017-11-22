"""Message api."""
from message.models import Message

def send_message(content:str, from_user: object, to_user: object, dialog: int) -> None:
    """Send message to user"""
    try:
        if dialog == 0:
            latest = Message.objects.latest()
            dialog = latest.dialog_id  + 1
        Message.objects.create(content=content, from_user=from_user, to_user=to_user, dialog_id=dialog)
    
    except Message.DoesNotExist:
        pass

def get_unread_messages(user:object) -> list:
    """Get unread user messages"""
    return Message.objects.unread(to_user=user)