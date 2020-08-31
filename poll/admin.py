from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Poll App Admin"

class ChoiceInLine(admin.TabularInline): 
    model = Choice 
    extra = 1
  
  
class QuestionAdmin(admin.ModelAdmin): 
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', { 
        'fields': ['pub_date'], 'classes': ['collapse']}), ] 
    inlines = [ChoiceInLine] 
  
  
admin.site.register(Question, QuestionAdmin) 