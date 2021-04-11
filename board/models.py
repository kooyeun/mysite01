from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models, OperationalError


def connection():
    return connect(user='webdb',
                     password='webdb',
                     host='localhost',
                     port=3306,
                     db='webdb',
                     charset='utf8')


def getBoardList():
    try:
        # 연결
        db = connection()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = '''
        select b.no, b.title, a.name, b.hit, date_format(b.reg_date,"%Y-%m-%d %p %h:%i:%s") as reg_datboard #6 글목록 들여쓰기 구현e, b.depth, b.del
            from user a, board b 
            where a.no=b.user_no 
        order by b.g_no desc, b.o_no asc
        '''
        cursor.execute(sql)

        # 결과 받아오기
        results = cursor.fetchall()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return results

    except OperationalError as e:
        print(f'error : {e}')


def getOneBoard(no):
    try:
        # 연결
        db = connection()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = '''
        select b.name, a.title, a.contents, a.g_no, a.o_no, a.depth, a.no, a.del
            from board a,user b
            where a.user_no=b.no
            and a.no=%s
        '''
        cursor.execute(sql,(no,))

        # 결과 받아오기
        result = cursor.fetchone()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return result

    except OperationalError as e:
        print(f'error : {e}')


def insertBoard(title,content,user_no):
    try:
        # connection
        db = connection()

        # cusor
        cursor = db.cursor()

        # SQL
        sql = 'insert into board values(null,%s,%s,0,now(),ifnull((select no from(select max(g_no) as no from board) as board_case),0)+1,1,0,%s,0)'
        count = cursor.execute(sql,(title,content,user_no))

        # commit
        db.commit()

        #
        cursor.close()
        db.close()

        #
        return count == 1

    except OperationalError as e:
        print(f'error : {e}')


def updateBoard(title, content, boardNo):
    try:
        # 연결
        db = connection()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'update board set title=%s,contents=%s where no=%s'
        count = cursor.execute(sql, (title, content, boardNo))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')


def deleteBoard(boardNo):
    try:
        # 연결
        db = connection()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = "update board set title='삭제된 글 입니다.',contents='작성자에 의해 삭제된 글입니다',hit=0,reg_date=now(),del=1 where no=%s"
        count = cursor.execute(sql, (boardNo,))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')