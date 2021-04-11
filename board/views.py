from math import ceil

from django.http import HttpResponseRedirect
from django.shortcuts import render

from board import models

# LIST_COUNT = 10


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


    boardList = models.getBoardList()
    data = {'boardList':boardList}

    del request.session["requestToken"]
    request.session["requestToken"] = 'indexPage'

    return render(request, 'board/index.html',data)


def view(request):
    # 정상적인 경로 접근 확인
    requestToken = request.session["requestToken"]
    if requestToken == 'indexPage' or requestToken == 'updateFormPage' or requestToken == 'replyFormPage':

        boardNo = request.GET.get("no")
        oneBoard = models.getOneBoard(boardNo)
        data = {'oneBoard':oneBoard}

        del request.session["requestToken"]
        request.session["requestToken"] = 'viewPage'

        return render(request, 'board/view.html', data)
    else:
        return HttpResponseRedirect('/board')


def writeform(request):
    # 정상적인 경로 접근 및 유저상태 확인
    requestToken = request.session["requestToken"]
    if (requestToken == 'indexPage' or requestToken == 'writeFormPage') and request.session.get("authuser") != None:

        del request.session["requestToken"]
        request.session["requestToken"] = 'writeFormPage'
        return render(request, 'board/writeform.html')
    else:
        return HttpResponseRedirect('/board')


def write(request):
    # 정상적인 경로 접근 및 유저상태 확인
    if request.session["requestToken"] == 'writeFormPage' and request.session.get("authuser") != None:
        title = request.POST["title"]
        content = request.POST["content"]

        # 빈칸으로 구성된 글 생성 체크
        if title != '' and content != '':
            userNo = request.session["authuser"]["no"]
            models.insertBoard(title,content,userNo)

            return HttpResponseRedirect('/board')
        else:
            return HttpResponseRedirect('/board/writeform')
    else:
        return HttpResponseRedirect('/board')


def updateform(request):
    # 정상적인 경로 접근 및 유저상태 확인
    if request.session["requestToken"] == 'viewPage' and request.session.get("authuser") != None:
        boardNo = request.GET["no"]
        oneBoard = models.getOneBoard(boardNo)

        # 글 작성자 본인 확인
        if request.session["authuser"]["no"] == oneBoard["user_no"] :
            data = { "oneBoard":oneBoard }

            del request.session["requestToken"]
            request.session["requestToken"] = 'updateFormPage'
            return render(request, 'board/updateform.html',data)
        else:
            return HttpResponseRedirect('/board/view')
    else:
        return HttpResponseRedirect('/board/view')


def update(request):
    # 정상적인 경로 접근 및 유저상태 확인
    if request.session["requestToken"] == 'updateFormPage' and request.session.get("authuser") != None:
        boardNo = request.POST["boardNo"]
        oneBoard = models.getOneBoard(boardNo)

        # 글 작성자 본인 확인
        if request.session["authuser"]["no"] == oneBoard["user_no"]:
            title = request.POST["title"]
            content = request.POST["content"]
            models.updateBoard(title,content,boardNo)

            return HttpResponseRedirect(f'/board/view?no={boardNo}')
        else:
            return HttpResponseRedirect('/board/view')
    else:
        return HttpResponseRedirect('/board/view')


def delete(request):
    # 정상적인 경로 접근 및 유저상태 확인
    if request.session["requestToken"] == 'indexPage' and request.session.get("authuser") != None:
        boardNo = request.GET["no"]
        oneBoard = models.getOneBoard(boardNo)

        # 글 작성자 본인 확인
        if request.session["authuser"]["no"] == oneBoard["user_no"]:
            models.deleteBoard(boardNo)
            return HttpResponseRedirect('/board')
        else:
            return HttpResponseRedirect('/board')
    else:
        return HttpResponseRedirect('/board')


def replyform(request):
    # 정상적인 경로 접근 및 유저상태 확인
    requestToken = request.session["requestToken"]
    if (requestToken == 'viewPage' or requestToken == 'replyFormPage') and request.session.get("authuser") != None:

        del request.session["requestToken"]
        request.session["requestToken"] = 'replyFormPage'
        return render(request, 'board/replyform.html')
    else:
        return HttpResponseRedirect('/board')


def reply(request):
    # 정상적인 경로 접근 및 유저상태 확인
    if request.session["requestToken"] == 'replyFormPage' and request.session.get("authuser") != None:
        title = request.POST["title"]
        content = request.POST["content"]
        originalBoardNo = request.POST["originalBoardNo"]

        # 빈칸으로 구성된 글 생성 체크
        if title != '' and content != '':
            originalBoard = models.getOneBoard(originalBoardNo)
            originalBoardG_no = originalBoard["g_no"]
            originalBoardO_no = originalBoard["o_no"]
            originalBoardDepth = originalBoard["depth"]
            models.updateForinsertReply(originalBoardG_no,originalBoardO_no)

            userNo = request.session["authuser"]["no"]
            models.insertForinsertReply(title,content,originalBoardG_no,originalBoardO_no,originalBoardDepth,userNo)

            return HttpResponseRedirect('/board')
        else:
            return HttpResponseRedirect(f'/board/replyform?no={originalBoardNo}')
    else:
        return HttpResponseRedirect('/board')

def search(request):

    keyword = request.POST["kwd"]
    searchedBoardList = models.getSearchedBoardList(keyword)
    data = {'boardList':searchedBoardList}

    del request.session["requestToken"]
    request.session["requestToken"] = 'indexPage'
    return render(request, 'board/index.html',data)

# 유저 상태 확인
#def checkUserState(request):
#    if request.session.get("authuser") == None :
#        return 'logout'
#    else :
#        if request.session["authuser"]["name"] ==