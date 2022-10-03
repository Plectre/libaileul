from ast import iter_child_nodes
from django.shortcuts import render
from .models import Location
from hangar import services
import datetime

def index(request):

    location = Location
    locations = location.objects.all()
    les_locations = hide_past_dates(locations)
    print(les_locations)

    locs = sort_dates(les_locations)

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

def sort_dates(dates):
    sorted_dates = []
    print(sorted_dates)