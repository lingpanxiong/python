from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
#
from django.shortcuts import render
import datetime

def current_datetime(request):
	now=datetime.datetime.now()
	t=get_template('current_datetime.html')
	stringa=["HTML","CSS","JS",]
	html=t.render(Context({'current_date': now,'string':stringa}))
	return HttpResponse(html)

def add2(request,a,b):
	c=int(a)+int(b)
	return HttpResponse(str(c))

def current_datetime1(request):
	
	stringa={'site':u'abc','content':u'bca'}
	return render(request,'current_datetime.html',{'string':stringa})