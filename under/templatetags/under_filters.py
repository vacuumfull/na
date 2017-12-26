from django import template

register = template.Library()

def callMethod(obj, methodName):
    
    method = getattr(obj, methodName)

    return method(obj.rate)


def arg(obj, arg):
    """Setting argument as propery of RatingManager"""
    setattr(obj, 'rate', int(arg))

    return obj
 

register.filter("call", callMethod)
register.filter("arg", arg)