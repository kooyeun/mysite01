from django.http import HttpResponseRedirect
from django.shortcuts import render

from guestbook import models


def index(request):
    results=models.findall()
    guestList={'guest_list':results}
    return render(request, 'guestbook/index.html',guestList)

def addGuestbook(request):
    name=request.POST["name"]
    password=request.POST["password"]
    message=request.POST["message"]

    models.insert(name,password,message)
    return HttpResponseRedirect('/guestbook')
