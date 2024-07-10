from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event


def event_detail_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})


def event_list_view(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


@login_required
def like_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user in event.liked_by.all():
        event.liked_by.remove(request.user)
        messages.success(request, f'You unliked {event.title}.')
    else:
        event.liked_by.add(request.user)
        messages.success(request, f'You liked {event.title}.')
    return redirect('events:event_detail', pk=event.id)
