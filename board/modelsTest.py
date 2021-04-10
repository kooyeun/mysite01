from board import models

def testBoardList():
    results = models.boardList()
    for result in results:
        print(result)

def testOneBoard():
    result=models.oneBoard(2)
    print(result)



#testBoardList()
testOneBoard()
