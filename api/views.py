"""Under api views."""
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from blog.models import Blog, Comment as BlogComment, Rating as BlogRating


def get_rating(request, sessionid: str, app: str, key: int):
    """Get app rating."""
    user = _get_user(sessionid)

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
    user = _get_user(sessionid)

    if not user:
        return JsonResponse({'error': 'User must be authenticated!'})

    try:
        if app == 'blog':
            blog = Blog.objects.get(pk=key)
            BlogRating.objects.create(blog=blog, user=user, value=vote)
    except (ObjectDoesNotExist, IntegrityError):
        pass

    return get_rating(request, sessionid, app, key)


def get_comment(request, sessionid: str, app: str, key: int, offset: int=0):
    """Get app comment."""
    result = {
        'comments': []
    }

    if app == 'blog':
        queryset = BlogComment.objects.get_last_comments(key, int(offset))

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
