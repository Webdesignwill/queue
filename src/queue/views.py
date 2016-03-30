from django.conf import settings
from django.shortcuts import render


def homeview(request):
    return render(request, 'index.html', {
        'fetch_interval': settings.FETCH_INTERVAL,
        'event': 'Event name'
    })
