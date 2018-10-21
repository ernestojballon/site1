from django.contrib import admin

from .models import Question,Choice

# models question and choice register to be edited with admin

admin.site.register(Question) 
admin.site.register(Choice)