from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template

def first(request):
	#t=get_template('first.html')
	html=('fist.html')
	return HttpResponse(html)