import imp
from django.contrib import admin

# Register your models here.

from .models import Topic # from the same directory as admin.py is in and file models import model Topic
admin.site.register(Topic) # manage model through the admin site
