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


def boardList():
    try:
        # 연결
        db = connection()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = '''
        select b.no, b.title, a.name, b.hit, date_format(b.reg_date,"%Y-%m-%d %p %h:%i:%s") as reg_date
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

def oneBoard(no):
    try:
        # 연결
        db = connection()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = '''
        select b.name, a.title, a.contents, a.g_no, a.o_no, a.depth
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