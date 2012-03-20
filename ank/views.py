#views.py
from django.http import HttpResponse
from ankiety.ank.models import Poll
from django.template import Context
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

def index(request):
    p = Poll.objects.all().order_by('-pubdate')[:5]
    
    return render_to_response('ank/index.html',{'Ankiety':p})

def detail(request, poll_id):
    ankieta = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('ank/detail.html', {'Ankieta':ankieta}) 

def showAll(request):
    allAnkiety = Poll.objects.all().order_by('-pubdate')

    return render_to_response('ank/all.html', {'Ankiety':allAnkiety})
            
def vote(request, choice_id):
    choice = get_object_or_404(Poll, pk=choice_id)
    choice.vote+=1
    return HttpResponse('sukces')
