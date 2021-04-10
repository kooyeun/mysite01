from board import models

def testBoardList():
    results = models.getBoardList()
    for result in results:
        print(result)

def testOneBoard():
    result=models.getOneBoard(2)
    print(result)

def insertBoard():
    models.insertBoard('title1','content1',5)

def updateBoard():
    models.updateBoard('x-title1','x-content',11)


if __name__ == '__main__' :

    # testOneBoard()
    # insertBoard()
    #updateBoard()
    testBoardList()