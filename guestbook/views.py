from django.shortcuts import render

from guestbook import models


def index(request):
    results=models.findall()
    guestList={'guest_list':results}
    return render(request, 'guestbook/index.html',guestList)