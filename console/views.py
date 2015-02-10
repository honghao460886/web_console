# -*- coding:utf8 -*-#
__author__ = 'honghao'

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template

from django.contrib.auth import authenticate, login as user_login, logout as user_logout


def home(request):
    # return render_to_response("index.html", {})
    t = get_template("index.html")
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        t = get_template("index.html")
        c = RequestContext(request, {'user': user})
        user_login(request, user)
        return HttpResponse(t.render(c))
    else:
        t = get_template("index.html")
        error = "username or password error!"
        c = RequestContext(request, {'error': error})
        return HttpResponse(t.render(c), {"error": error})


def logout(request):
    user_logout(request)
    t = get_template("index.html")
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))