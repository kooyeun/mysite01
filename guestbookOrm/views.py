from django.http import HttpResponseRedirect
from django.shortcuts import render

from guestbookOrm.models import Guestbook


def index(request):
    results=Guestbook.objects.all().order_by('-id')
    guestList={'guest_list': results}
    return render(request,'guestbookOrm/index.html',guestList)

def addGuestbook(request):
    guestbook=Guestbook()
    guestbook.name=request.POST["name"]
    guestbook.password=request.POST["password"]
    guestbook.message=request.POST["message"]

    guestbook.save()

    return HttpResponseRedirect("/guestbookOrm")
