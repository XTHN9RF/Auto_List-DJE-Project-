from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def cookie(request):
    print(request.COOKIES)
    old_value = request.COOKIES.get('zap', None)
    resp = HttpResponse('In a view - the zap cookie value is ' + str(old_value))
    if old_value:
        resp.set_cookie('zap', int(old_value) + 1)
    else:
        resp.set_cookie('zap', 42)
    resp.set_cookie('sakaicar', 42, max_age=1000)
    return resp


def session_view(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4:
        del (request.session['num_visits'])
    context = {'num_visits': int(num_visits)}
    return render(request, "hello/hello.html", context)
