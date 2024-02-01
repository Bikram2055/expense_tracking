from django.contrib import admin
from .models import Category, Expenses, Record
from django.contrib.sessions.models import Session


# Register your models here.
admin.site.register(Record)
admin.site.register(Category)
admin.site.register(Expenses)
admin.site.register(Session)