from django.shortcuts import render, redirect, get_object_or_404
from .models import Venue
from .forms import VenueForm

def venue_list(request):
    # Filter by sport type
    sport_type = request.GET.get('sport_type', '')
    # Filter by location
    location = request.GET.get('location', '')
    # Filter by booking status (either True for available or False for booked)
    booking_status = request.GET.get('booking_status', '')

    venues = Venue.objects.all()

    if sport_type:
        venues = venues.filter(sport_type__icontains=sport_type)
    if location:
        venues = venues.filter(location__icontains=location)
    if booking_status:
        booking_status = True if booking_status == 'available' else False
        venues = venues.filter(booking_status=booking_status)

    return render(request, 'venue_list.html', {'venues': venues})

def venue_create(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venue_list')
    else:
        form = VenueForm()
    return render(request, 'venue_form.html', {'form': form})

def venue_update(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    if request.method == 'POST':
        form = VenueForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            return redirect('venue_list')
    else:
        form = VenueForm(instance=venue)
    return render(request, 'venue_form.html', {'form': form})

def venue_delete(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    if request.method == 'POST':
        venue.delete()
        return redirect('venue_list')
    return render(request, 'venue_confirm_delete.html', {'venue': venue})
