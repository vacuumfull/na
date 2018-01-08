"""Under api views."""
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

import blog.api
import event.api
import place.api
import band.api
import message.api
import member.api



def get_users(request, sessionid: str):
    """Get users"""
    user = _get_user(sessionid)
    if not user:
        return JsonResponse({'error': 'User must be authenticated!'})

    usernames = User.objects.values('username')
    list_users = [entry for entry in usernames]
    
    return JsonResponse(list_users, safe=False)


def get_locations(request):
    """Get places locations"""
    result = {}
    result = getattr(_load_module('place'), 'get_locations')()
  
    return JsonResponse(result, safe=False)


def get_rating(request, key: int, app: str):
    result = {}
    result = getattr(_load_module(app), 'get_rate_unlogin')(key)

    return JsonResponse(result)


def get_user_settings(request, sessionid: str):
    user = _get_user(sessionid)
    if not user:
        return JsonResponse({'error': 'User must be authenticated!'})

    result = {}
    result = getattr(_load_module('member'), 'get_settings')(user)

    return JsonResponse(result)


def get_messages_history(request, dialog:int, sessionid:str, offset:int):
    """Get messages history"""
    user = _get_user(sessionid)
    if not user:
        return JsonResponse({'error': 'User must be authenticated!'})

    result = {}
    result = getattr(_load_module('message'), 'get_messages_history')(int(dialog), int(offset))

    return JsonResponse(result, safe=False)


def get_dialogs(request, sessionid:str):
    """Get muser dialogs"""
    user = _get_user(sessionid)
    if not user:
        return JsonResponse({'error': 'User must be authenticated!'})

    result = getattr(_load_module('message'), 'get_dialogs')(user)

    return JsonResponse(result, safe=False)


def search_default(request, keyword:str):
    keyword = 'techno'
    result = {
                'id': 121,
                'type':'event',
                'title': 'Local Techno',
                'description': 'Local Techno овзвращается в город',
                'image': '/static/events/poster/local.bmp',
                'date': '2018-01-18',
                'price': '300',
                'tags': 'techno, localtechno',
                'slug': 'local_techno_return',
                'created_at': '2018-01-01',
                'owner': 'Kosenkoff',
            }
    return JsonResponse(result)


def search_type(request, app:str, keyword:str):
    print('searched type')
    app = 'event'
    keyword = 'techno'
    result = {
        '1':{
            'id': 121,
            'title': 'Local Techno',
            'description': 'Local Techno овзвращается в город',
            'image': '/static/events/poster/local.bmp',
            'date': '2018-01-18',
            'price': '300',
            'tags': 'techno, localtechno',
            'slug': 'local_techno_return',
            'created_at': '2018-01-01',
            'owner': 'Kosenkoff',
        },
        '2': {
            'id': 130,
            'title': 'Gamma Festival',
            'description': 'Логос анонсировал начало Гамма Фестиваля',
            'image': '/static/events/poster/local.bmp',
            'date': '2018-06-22',
            'price': '2100',
            'tags': 'techno, gammafestival, m_division',
            'slug': 'gammafestivalagain',
            'created_at': '2018-01-01',
            'owner': 'Logos',
        }
    }
    return JsonResponse(result)



def search_tags(request, keyword:str):
    """вывод похожих тэгов по ключу. Можно ограничить 30"""
    print('fast search')
    keyword = 'пизд'
    result = ('пиздюк', 'пиздец', 'пиздюли', 'пиздэйшен', 'пиздаболка', 'пизда')
    return JsonResponse(result, safe=False)


def get_tags(request):
    """Вывод самых попоулярных тэгов с указанием количества. Макс - 1000. Запрос стоит сделать кэшиуремым"""

    result = {'first searched tag': 113, 'second searched tag': 99, 'third searched tag': 87}
    return JsonResponse(result)


@csrf_exempt
@require_http_methods(['POST'])
def update_user_settings(request): 
    sessionid = request.POST.get('sessionid')
    comment = request.POST.get('comment')
    blog = request.POST.get('blog')
    rating = request.POST.get('rating')
    link = request.POST.get('link')
    
    params = {
        'comment': comment,
        'blog': blog,
        'rating': rating,
        'link': link
    }
    user = _get_user(sessionid)

    if not user:
        return JsonResponse({'error': 'User must be authenticated!'})
    
    getattr(_load_module('member'), 'update_settings')(user, params)

    result = {'success': 'Settings successfully updated'}

    return JsonResponse(result)


@csrf_exempt
@require_http_methods(['POST'])
def update_user_prefer_styles(request): 
    """Update user prefer styles in extends"""
    sessionid = request.POST.get('sessionid')
    styles = json.loads(request.POST.get('styles'))
    user = _get_user(sessionid)
    if not user:
        return JsonResponse({'error': 'User must be authenticated!'})
    
    getattr(_load_module('member'), 'update_prefer_styles')(user, styles)
    result = {'success': 'Prefer styles successfully updated'}    

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


def get_comment(request, app: str, key: int, offset: int=0):
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


def list_items(request, app: str, sessionid: str):
    """Get user created items list"""
    user = _get_user(sessionid)
    if not user:
        return JsonResponse({'error': 'User must be authenticated!'})

    result = {}
    result = getattr(_load_module(app), 'list_items')(user)

    return JsonResponse(result, safe=False)

    
@csrf_exempt
@require_http_methods(['POST'])
def remove_item(request):
    """Get user created items list"""
    sessionid = request.POST.get('sessionid')
    app = request.POST.get('app')
    item_id = request.POST.get('item_id')
    user = _get_user(sessionid)
    if not user:
        result = {'error': 'User must be authenticated!'}

    getattr(_load_module(app), 'remove_item')(int(item_id))
    result = {'success': 'Item successfully removed'}

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

    request.session['last_comment'] = datetime.now().strftime(r'%x %X')
    if not result.get('error'):
        getattr(_load_module(app), 'send_comment')(key, user, content)
        result = {'success': 'Comment success append'}
    return JsonResponse(result)



@csrf_exempt
@require_http_methods(['POST'])
def send_message(request):
    sessionid = request.POST.get('sessionid')
    login = request.POST.get('login')
    content = request.POST.get('content', '')
    dialog = request.POST.get('dialog')
    from_user = _get_user(sessionid)
    to_user = _get_message_getter(login)
    last_message = request.session.get('last_message')
    result = {}

    if not from_user:
        result = {'error': 'User must be authenticated!'}

    if not content.strip():
        result = {'error': 'Content not be empty!'}

    if last_message:
        last_message = datetime.strptime(last_message, r'%x %X')
        if datetime.now() - last_message < timedelta(seconds=15):
            result = {'error': 'Too many query per minutes!'}

    request.session['last_message'] = datetime.now().strftime(r'%x %X')
    if not result.get('error'):
        info = {}
        info = getattr(_load_module('message'), 'send_message')(content, from_user, to_user, int(dialog))
        result = {'success': 'Message successly send', 'info': info}

    return JsonResponse(result)


@csrf_exempt
@require_http_methods(['POST'])
def read_messages(request):
    sessionid = request.POST.get('sessionid')
    dialog_id = request.POST.get('dialog')
    user = _get_user(sessionid)
    result = {}

    if not user:
        result = {'error': 'User must be authenticated!'}

    if not result.get('error'):
        getattr(_load_module('message'), 'read_messages')(user, int(dialog_id))
        result = {'success': 'Successfully red messages'}
    
    return JsonResponse(result)


@csrf_exempt
@require_http_methods(['POST'])
def remove_message(request):
    sessionid = request.POST.get('sessionid')
    message_id = request.POST.get('message_id')
    user = _get_user(sessionid)
    result = {}

    if not user:
        result = {'error': 'User must be authenticated!'}
    
    if not result.get('error'):
        getattr(_load_module('message'), 'remove_message')(int(message_id))
        result = {'success': 'Message successfully removed'}

    return JsonResponse(result)




def _get_user(sessionid):
    """Get user info from sessionid token."""
    session = SessionStore(sessionid)
    try:
        user = User.objects.get(id=session.get('_auth_user_id'))
    except User.DoesNotExist:
        user = None

    return user


def _get_message_getter(login):
    try:
        user = User.objects.get(username=login)
    except User.DoesNotExists:
        user = None

    return user


def _load_module(module_name: str) -> object:
    """Load module api from string."""
    module_dict = {
        'blog': blog.api,
        'event': event.api,
        'place': place.api,
        'band': band.api,
        'message': message.api,
        'member': member.api
    }

    return module_dict[module_name]