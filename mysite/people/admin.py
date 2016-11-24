from django.contrib import admin

# Register your models here.
'''
class ArtcleAdmin(admin.ModelAdmin):
	list_filter=('title')
'''
from .models import Article,person
admin.site.register(Article)
admin.site.register(person)