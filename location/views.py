from ast import iter_child_nodes
from django.shortcuts import render
from .models import Location
import datetime

def index(request):

    location = Location
    locations = location.objects.all()
    les_locations = hide_past_dates(locations)

    context = {
            'locations': les_locations,
        }
    return render(request, 'location/index.html', context)

## Gestion des dates revolues pour ne pas les affichées
def hide_past_dates(locs):
    locations = []
    for loc in locs:
        if datetime.date.today() > loc.end.date():
            pass
        else:
            locations.append(loc)
            print (locations)
    return locations
