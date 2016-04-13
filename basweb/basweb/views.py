#!coding utf-8
#from django.http import HttpResponse
from django.shortcuts import render_to_response

def first(request):
	#t=get_template('first.html')
	return render_to_response('first.html')


def second(request):
	#t=get_template('first.html')
	return render_to_response('second.html')