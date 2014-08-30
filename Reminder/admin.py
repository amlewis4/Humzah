from django.contrib import admin
from Reminder.models import List
from Reminder.models import category

class ListAdmin(admin.ModelAdmin):
	list_display = ('category')


class categoryAdmin(admin.ModelAdmin):
	list_display = ('Reminder, pub_date')