from ast import iter_child_nodes
from django.shortcuts import render
from .models import Location

def index(request):

    location = Location
    locations = location.objects.all()

    context = {
            'locations': locations,
        }
    iter_locations(locations)
    return render(request, 'location/index.html', context)

def iter_locations(locs):
    for loc in locs:
        print(f'start-> {loc.start} : end-> {loc.end}')