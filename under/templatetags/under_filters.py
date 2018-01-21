from django import template
from django.contrib.auth.models import Group


register = template.Library()

def callMethod(obj, methodName):
    
    method = getattr(obj, methodName)

    return method(obj.rate)


def arg(obj, arg):
    """Setting argument as propery of RatingManager"""

    setattr(obj, 'rate', int(arg))

    return obj


def has_group(user, group_name):
    group =  Group.objects.get(name=group_name) 
    return group in user.groups.all() 
 

def to_pipe_string(tags):
    """Tags objects filter if not string."""
    if not isinstance(tags, str):
        tags = ','.join(tag.name for tag in tags)
    return tags


register.filter("call", callMethod)
register.filter("arg", arg)
register.filter("has_group", has_group)
register.filter("to_pipe_string", to_pipe_string)