#view.py

from django.http import HttpResponse
import datetime
from django.template import Template,Context

def current_datetime(request,dt):
	#dt=int(dt)
	#da=dt+2
	#html= "<html><body>this is %s of  %s page!</body></html>"%(dt,da)
	t= Template('hello,{{name}}')
	html= t.render(Context({'name':'john'}))
	return HttpResponse(html)
def muban(request):
	t= Template('company,{{name}}')
	companyname= t.render(Context({'name':'avc'}))
	return HttpResponse(companyname)