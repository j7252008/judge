from django.shortcuts import render


# Create your views here.
#coding=utf-8

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from hwoj.models import User, Question

#表单
class UserForm(forms.Form):

	username = forms.CharField(label='用户名', max_length=50)
	password = forms.CharField(label='密码', max_length=50)

#注册
def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username=username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()

    return render(request, 'regist.html', {'uf':uf})

#登录
def login(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			#获取表单用户密码
			username=uf.cleaned_data['username']
			password=uf.cleaned_data['password']

			#获取表单数据与数据库比较
			user=User.objects.filter(username__exact=username, password__exact=password)
			if user:
				questions = Question.objects.all()
				response=render(request, 'home.html', {'questions': questions})
				#response=HttpResponseRedirect('/home', context)
				response.set_cookie('username', username, 3600)
				return response
			else:
				return HttpResponseRedirect('/')
	else:
		uf=UserForm()
		return render(request, 'login.html', {'uf':uf})

#登录成功
def home(request):
	username=request.COOKIES.get('username')

	if username:	
		return render(request, 'home.html', {'username':username})
	else:
		uf=UserForm()
		return HttpResponseRedirect('/', uf)