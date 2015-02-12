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
    print username
    if username is None or username == '':
        t = get_template("index.html")
        error = "用户名不能为空，请输入用户名！"
        c = RequestContext(request, {'error': error})
        return HttpResponse(t.render(c), {"error": error})
    password = request.POST.get('password')
    if password is None or password == '':
        t = get_template("index.html")
        error = "密码不能为空，请输入密码！"
        c = RequestContext(request, {'error': error})
        return HttpResponse(t.render(c), {"error": error})
    user = authenticate(username=username, password=password)
    if user is not None:
        t = get_template("index.html")
        c = RequestContext(request, {'user': user})
        user_login(request, user)
        return HttpResponse(t.render(c))
    else :
        t = get_template("index.html")
        error = "用户名或密码输入错误！"
        c = RequestContext(request, {'error': error})
        return HttpResponse(t.render(c), {"error": error})


def logout(request):
    user_logout(request)
    t = get_template("index.html")
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))