from django.http import HttpResponse
from ankiety.ank.models import Poll
from django.template import Context
from django.shortcuts import render_to_response


def index(request):
    p = Poll.objects.all().order_by('-pubdate')[:5]
    
    return render_to_response('ank/index.html',{'Ankiety':p})

def detail(request, poll_id)
    pass
    
