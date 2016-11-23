# coding:utf-8
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

from django.shortcuts import render
import datetime


def current_datetime(request):
	now=datetime.datetime.now()
	t=get_template('current_datetime.html')
	html=t.render(Context({'current_date':now}))
	return HttpResponse(html)

def add2(request,a,b):
	c=int(a)+int(b)
	return HttpResponse(str(c))

def current_datetime1(request):
	
	stringa={'site':u'abc','content':u'bca'}
	return render(request,'current_datetime.html',{'string':stringa})

from people.forms import AddForm
def index(request):
	if request.method=='POST':
		form=AddForm(request.POST)
#form.is_valid() must include '()'
		if form.is_valid():
			a=form.cleaned_data['a']
			b=form.cleaned_data['b']
			return HttpResponse(str(int(a)+int(b)))

	else:
		form=AddForm()
	return render(request,'index.html',{'form':form})