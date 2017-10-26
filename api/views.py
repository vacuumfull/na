"""Under api views."""
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from blog.models import Blog, Rating as BlogRating


def get_rating(request, sessionid: str, app: str, key: int):
    """Get app rating."""
    session = SessionStore(sessionid)
    try:
        user = User.objects.get(id=session.get('_auth_user_id'))
    except User.DoesNotExist:
        user = None

    result = {}
    if app == 'blog':
        result = BlogRating.objects.average(key, user)

    return JsonResponse(result)


@csrf_exempt
@require_http_methods(['POST'])
def vote_rating(request):
    """Get app rating."""
    sessionid = request.POST.get('sessionid')
    app = request.POST.get('app')
    key = request.POST.get('key')
    vote = int(request.POST.get('vote', 5))
    session = SessionStore(sessionid)

    try:
        user = User.objects.get(id=session.get('_auth_user_id'))
    except User.DoesNotExist:
        return {'error': 'User must be authenticated!'}

    try:
        if app == 'blog':
            blog = Blog.objects.get(pk=key)
            BlogRating.objects.create(blog=blog, user=user, value=vote)
    except (ObjectDoesNotExist, IntegrityError):
        pass

    return get_rating(request, sessionid, app, key)
