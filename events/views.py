from django.shortcuts import render
from .models import Event


def events_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/events_list.html', {'events': events})
