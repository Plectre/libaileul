
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect

import logbook
from .forms import FormLogBook
from .models import LogBook


def index(request):

    ## request of Logbook by 'username'
    logs = LogBook.objects.filter(user=request.user.username)

    context = {
        'logs':logs,
    }
    return render(request, 'logbook/index.html', context)


def form(request):
    if request.method == 'POST':
        form = FormLogBook(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/logbook/")
    else:
        form = FormLogBook()
        
    return render(request, 'logbook/form.html', {'form': form})


def delete(request, log_id):
    LogBook.objects.filter(id=log_id).delete()
    return HttpResponseRedirect("/logbook/")