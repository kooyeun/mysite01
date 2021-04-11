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


    boardList = models.getBoardList()
    data = {'boardList':boardList}

    return render(request, 'board/index.html',data)


def view(request):
    # 유저 상태 확인


    boardNo = request.GET["no"]
    oneBoard = models.getOneBoard(boardNo)
    data = {'oneBoard':oneBoard}
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


def updateform(request):
    # 유저 상태 확인

    boardNo = request.GET["no"]
    oneBoard = models.getOneBoard(boardNo)
    data = { "oneBoard":oneBoard }

    return render(request, 'board/updateform.html',data)


def update(request):
    # 유저 상태 확인

    boardNo = request.POST["boardNo"]
    title = request.POST["title"]
    content = request.POST["content"]
    models.updateBoard(title,content,boardNo)

    return HttpResponseRedirect(f'/board/view?no={boardNo}')


def delete(request):
    # 유저 상태 확인

    boardNo = request.GET["no"]
    models.deleteBoard(boardNo)

    return HttpResponseRedirect('/board')


def replyform(request):
    # 유저 상태 확인

    return render(request, 'board/replyform.html')


def reply(request):
    # 유저 상태 확인

    originalBoardNo = request.POST["originalBoardNo"]
    originalBoard = models.getOneBoard(originalBoardNo)
    originalBoardG_no = originalBoard["g_no"]
    originalBoardO_no = originalBoard["o_no"]
    originalBoardDepth = originalBoard["depth"]
    models.updateForinsertReply(originalBoardG_no,originalBoardO_no)

    title = request.POST["title"]
    content = request.POST["content"]
    userNo = request.session["authuser"]["no"]
    models.insertForinsertReply(title,content,originalBoardG_no,originalBoardO_no,originalBoardDepth,userNo)

    return HttpResponseRedirect('/board')


# 유저 상태 확인
def checkUserState(request):
    pass