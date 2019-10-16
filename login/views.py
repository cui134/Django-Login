# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from . import models
from . import forms
from login.utils.BaseView import AuthenticateView
# Create your views here.

class IndexView(AuthenticateView):
    def get(self, request):
        return render(request, 'login/index.html')


def LoginView(request):
    print "login request user:", request.user
    if request.user.is_authenticated:
        return redirect('/index/')

    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            auth_user = authenticate(request, username=username, password=password)
            if auth_user:
                print "auth_user:", auth_user.username
                login(request, auth_user)
                return redirect('/index/')
            else:
                message = '密码不正确或者用户不存在！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())



def Register(request):
    pass
    return render(request, 'login/register.html')

class LogoutView(AuthenticateView):
    def get(self, request):
        logout(request)
        return redirect("/login/")