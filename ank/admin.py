from django.contrib import admin
from ankiety.ank.models import Poll
from ankiety.ank.models import Choice 

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class PollAdmin (admin.ModelAdmin):
    fields = ['pubdate', 'question']
    inlines = [ChoiceInline]

    date_hierachy = 'pubdate'
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
        
        
    
