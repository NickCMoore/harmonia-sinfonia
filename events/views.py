from django.shortcuts import render, get_object_or_404
from .models import Event


def event_detail_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})


def event_list_view(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})
