#coding:utf-8
from __future__ import unicode_literals

from django.db import models
#add form me
from django.contrib import admin

# Create your models here.
#admin username:iront password:pass539966;
#python manage.py createsuperuser to create a administror

#ForeignKey,ManyToManyField,OneToOneField:多对一，多对多，一对一



class Article(models.Model):
	title=models.CharField(u'标题',max_length=256)
	content=models.TextField(u'内容')
	autor=models.ManyToManyField('person') #person未定义前需加''

	pub_date=models.DateTimeField(u'发布时间',auto_now_add=True,editable=True)
	update_time=models.DateTimeField(u'更新时间',auto_now=True,null=True)
	
#__unicode__ include 4 "_"
	def __unicode__(self):
		return self.title

class person(models.Model):
	name=models.CharField(max_length=32)
	age=models.IntegerField()
	def __unicode__(self):
		return self.name
#add search
'''
class persona(models.Model):
	
	search_fields=('name',)
'''