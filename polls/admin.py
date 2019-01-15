from django.contrib import admin

from .models import Choice, Poll, Vote

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3

# Register your models here.
admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Vote)
