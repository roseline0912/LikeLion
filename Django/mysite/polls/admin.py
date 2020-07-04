from django.contrib import admin
from .models import Question, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)

#pyhon manage.py createsuperuser
# username:msjang
# email address:
# password:12345678