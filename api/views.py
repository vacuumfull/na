"""Under api views."""
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

import blog.api


def get_rating(request, sessionid: str, app: str, key: int):
    """Get app rating."""
    user = _get_user(sessionid)

    result = {}
    result = getattr(_load_module(app), 'get_rating')(key, user)

    return JsonResponse(result)


@csrf_exempt
@require_http_methods(['POST'])
def vote_rating(request):
    """Vote for app and get updated rating."""
    sessionid = request.POST.get('sessionid')
    app = request.POST.get('app')
    key = request.POST.get('key')
    vote = int(request.POST.get('vote', 5))
    user = _get_user(sessionid)

    if not user:
        result = JsonResponse({'error': 'User must be authenticated!'})

    if vote > 10:
        # Anticheat system
        vote = 0

    getattr(_load_module(app), 'vote_rating')(key, user, vote)

    result = get_rating(request, sessionid, app, key)
    return result


def get_comment(request, sessionid: str, app: str, key: int, offset: int=0):
    """Get app comment."""
    result = {
        'comments': []
    }

    queryset = getattr(_load_module(app), 'get_comment')(key, offset)

    for query in queryset:
        result['comments'].append({
            'user': query.user.username,
            'content': query.content,
            'datetime': str(query.created_at),
        })
    return JsonResponse(result)


@csrf_exempt
@require_http_methods(['POST'])
def send_comment(request):
    """Send app comment and get updated rating."""
    sessionid = request.POST.get('sessionid')
    app = request.POST.get('app')
    key = request.POST.get('key')
    content = request.POST.get('content', '')
    user = _get_user(sessionid)
    last_comment = request.session.get('last_comment')
    result = {}

    if not user:
        result = {'error': 'User must be authenticated!'}

    if not content.strip():
        result = {'error': 'Content not be empty!'}

    if last_comment:
        last_comment = datetime.strptime(last_comment, r'%x %X')
        if datetime.now() - last_comment < timedelta(seconds=30):
            result = {'error': 'Too many query per minutes!'}

    if len(content) > 250:
        result = {'error': 'Comment must be less 250 chars!'}

    getattr(_load_module(app), 'send_comment')(key, user, content)
    request.session['last_comment'] = datetime.now().strftime(r'%x %X')

    if not result.get('error'):
        result = {'success': 'Comment add'}
    return JsonResponse(result)


def _get_user(sessionid):
    """Get user info from sessionid token."""
    session = SessionStore(sessionid)
    try:
        user = User.objects.get(id=session.get('_auth_user_id'))
    except User.DoesNotExist:
        user = None

    return user


def _load_module(module_name: str) -> object:
    """Load module api from string."""
    module_dict = {
        'blog': blog.api,
    }

    return module_dict[module_name]
