from django.contrib import admin
from .models import Question, Choice

# Register your models here.

admin.site.site_header = "Poll Admin"
admin.site.site_title = "Poll Admin Area"
admin.site.index_title = "This is the Poll App Admin area"

# Tabular inline models, allow you to control the display of certain elements with a linked class

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # Fieldsets takes in a name for the field
    # and the fields to display, no name needed here
    fieldsets = [((None), {'fields': ['question_text']}),
    ('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
