#view.py

from django.http import HttpResponse
#import datetime
from django.template import Template,Context

def people(request):
	t= Template('hello,{{name}}')
	html= t.render(Context({'name':'john'}))
	return HttpResponse(html)
def muban(request):
	t= Template('company,{{name}}')
	companyname= t.render(Context({'name':'avc'}))
	return HttpResponse(companyname)