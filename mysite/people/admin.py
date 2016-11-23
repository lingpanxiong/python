from django.contrib import admin

# Register your models here.
'''
class ArtcleAdmin(admin.ModelAdmin):
	list_filter=('title')
'''
from .models import Article
admin.site.register(Article)