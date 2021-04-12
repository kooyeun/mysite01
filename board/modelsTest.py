from board import models

def testBoardList():
    results = models.getBoardList()
    for result in results:
        print(result)

def testOneBoard():
    result=models.getOneBoard(2)
    print(result)
    print(f'name : {result["name"]}')

def insertBoard():
    models.insertBoard('title1','content1',5)

def updateBoard():
    models.updateBoard('x-title1','x-content',11)

def deleteBoard():
    models.deleteBoard(10)

def updateForReply():
    models.updateForinsertReply(6,1)

def insertForReply():
    models.insertForinsertReply('insert reply test01','test',6,1,0,5)

def getSearchedBoardList():
    results = models.getSearchedBoardList('test')
    for result in results:
        print(result)

def updateBoardView(boardNo):
    models.updateBoardView(boardNo)

if __name__ == '__main__' :

    # testOneBoard()
    # insertBoard()
    #updateBoard()
    #deleteBoard()
    # updateForReply()
    #insertForReply()
    #getSearchedBoardList()
    #updateBoardView(9)
    testBoardList()