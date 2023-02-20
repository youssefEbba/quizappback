from django.forms import TextInput
from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from django.contrib import admin
from django.db import models
from django import forms
from django.forms import Textarea
from .models  import Quiz ,Participation ,Question, User
class ChoiceInline(admin.TabularInline):
    model = Question
    extra = 3
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'15'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':30})},
    }

    
class QuizAdmin(admin.ModelAdmin):
    fieldsets =[
        (None, {'fields': ['titre']}),
        (1, {'fields': ['categorie']}),
        ('Date information', {'fields': ['date'], 'classes': ['collapse']}),
      (2, {'fields': ['duree']})
    ]
    inlines = [ChoiceInline]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
class QustionAdmin(admin.ModelAdmin):
     fieldsets =[]
     formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(Quiz,QuizAdmin)
admin.site.register(Participation)
admin.site.register(Question,QustionAdmin)
admin.site.register(User)
TokenAdmin.raw_id_fields = ['user']