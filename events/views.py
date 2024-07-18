from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Event
from django.core.paginator import Paginator

def event_detail_view(request, pk):
    """Display the details of a specific event."""
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def event_list_view(request):
    """Display a list of all events with pagination."""
    events = Event.objects.all().order_by('-date')
    paginator = Paginator(events, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'events/event_list.html', {'page_obj': page_obj})

@login_required
def like_event(request, event_id):
    """Allow a logged-in user to like or unlike an event."""
    try:
        event = get_object_or_404(Event, id=event_id)
        if request.user in event.liked_by.all():
            event.liked_by.remove(request.user)
            messages.success(request, f'You unliked {event.title}.')
        else:
            event.liked_by.add(request.user)
            messages.success(request, f'You liked {event.title}.')
    except Event.DoesNotExist:
        messages.error(request, "The event you are trying to like does not exist.")
    except ValidationError as e:
        messages.error(request, f"Error during liking the event: {e}")
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {e}")

    return redirect('events:event_detail', pk=event.id)
