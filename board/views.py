from math import ceil

from django.http import HttpResponseRedirect
from django.shortcuts import render

from board import models

LIST_COUNT = 10


def index(request):
    # page = request.GET.get("p")
    # page = 1 if page is None else int(page)

    # print(page)

    # totalcount = models.count()
    # boardlist = models.findall(page, LIST_COUNT)

    # paging 정보를 계산
    # pagecount = ceil(totalcount / LIST_COUNT)
    #
    # data = {
    #     "boardlist": boardlist,
    #     'pagecount': pagecount,
    #     'netpage': 7,
    #     'prvpage': 5,
    #     'curpage': 2
    #
    # }

    # 유저 상태 확인


    boardList = models.boardList()
    data = {'boardList':boardList}

    return render(request, 'board/index.html',data)


def view(request):
    # 유저 상태 확인


    no = request.GET["no"]
    result = models.oneBoard(no)
    data = {'oneBoard':result}
    return render(request, 'board/view.html', data)


def writeform(request):
    # 유저 상태 확인

    return render(request, 'board/writeform.html')


def write(request):
    # 유저 상태 확인

    title = request.POST["title"]
    content = request.POST["content"]
    userNo = request.session["authuser"]["no"]
    models.insertBoard(title,content,userNo)

    return HttpResponseRedirect('/board')




# 유저 상태 확인
def checkUserState(request):
    pass