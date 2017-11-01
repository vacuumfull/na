"""Under api views."""
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from blog.api import blog_rating, vote_blog_rating, blog_comment


def get_rating(request, sessionid: str, app: str, key: int):
    """Get app rating."""
    user = _get_user(sessionid)

    result = {}
    if app == 'blog':
        result = blog_rating(key, user)

    return JsonResponse(result)


@csrf_exempt
@require_http_methods(['POST'])
def vote_rating(request):
    """Get app rating."""
    sessionid = request.POST.get('sessionid')
    app = request.POST.get('app')
    key = request.POST.get('key')
    vote = int(request.POST.get('vote', 5))
    user = _get_user(sessionid)

    if not user:
        result = JsonResponse({'error': 'User must be authenticated!'})

    if app == 'blog':
        vote_blog_rating(key, user, vote)

    result = get_rating(request, sessionid, app, key)
    return result


def get_comment(request, sessionid: str, app: str, key: int, offset: int=0):
    """Get app comment."""
    result = {
        'comments': []
    }

    if app == 'blog':
        queryset = blog_comment(key, offset)

    for query in queryset:
        result['comments'].append({
            'user': query.user.username,
            'content': query.content,
            'datetime': str(query.created_at),
        })
    return JsonResponse(result)


def _get_user(sessionid):
    """Get user info from sessionid token."""
    session = SessionStore(sessionid)
    try:
        user = User.objects.get(id=session.get('_auth_user_id'))
    except User.DoesNotExist:
        user = None

    return user
