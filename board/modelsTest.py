from board import models

def testBoardList():
    results = models.boardList()
    for result in results:
        print(result)

def testOneBoard():
    result=models.oneBoard(2)
    print(result)

def insertBoard():
    models.insertBoard('title1','content1',5)


if __name__ == '__main__' :

    # testOneBoard()
    # insertBoard()
    testBoardList()