from django.shortcuts import render

from guestbookOrm.models import Guestbook


def index(request):
    results=Guestbook.objects.all().order_by('-regdate')
    guestList={'guest_list': results}
    return render(request,'guestbookOrm/index.html',guestList)
