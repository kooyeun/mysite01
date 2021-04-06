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

def deleteForm(request):
    return render(request,'guestbook/deleteform.html')

def deleteGuestbook(request):
    no = request.POST["no"]
    password = request.POST["password"]

    models.deleteby_no_and_password(no,password)
    return HttpResponseRedirect('/guestbook')

