"""Message api."""
from message.models import Message


def send_message(content:str, from_user: object, to_user: object, dialog: int):
    """Send message to user"""
    try:
        info = {}
        if dialog == 0:
            latest = Message.objects.latest()
            dialog = latest.dialog_id  + 1
            info = {'dialog_id': dialog, 'username': from_user.username}
        Message.objects.create(content=content, from_user=from_user, to_user=to_user, dialog_id=dialog)
        return info
    except Message.DoesNotExist:
        pass


def get_unread_messages(user:object) -> list:
    """Get unread user messages"""
    return Message.objects.unread(to_user=user)


def get_messages_history(dialog:int, offset:int) -> list:
    """Get messages history"""
    return Message.objects.dialog_history(dialog, offset)


def get_dialogs(user:object) -> list:
    """Get user dialogs"""
    return Message.objects.dialogs(user)


def read_messages(user:object, dialog:int) -> None:
    """Set messages read"""
    try:
        Message.objects.filter(dialog_id=dialog, to_user=user).update(read=True)
    except Message.DoesNotExist:
        pass

def remove_message(message_id:int) -> None:
    """Remove message by id"""
    try:
        Message.objects.filter(id=message_id).update(deleted=True)
    except Message.DoesNotExist:
        pass