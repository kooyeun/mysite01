from MySQLdb import connect,OperationalError
from MySQLdb.cursors import DictCursor


def findall():
    try:
        # connection
        db = conn()

        # cusor
        cursor = db.cursor(DictCursor)

        # SQL
        sql = '''
        select no,
		        name,
		        message,
                date_format(reg_date,"%Y-%m-%d %p %h:%i:%s") as reg_date
	        from guestbook
        order by reg_date desc
        '''
        cursor.execute(sql)

        # result
        results = cursor.fetchall()

        #
        cursor.close()
        db.close()

        #
        return results

    except OperationalError as e:
        print(f'error : {e}')


def insert(name,password,message):
    try:
        # connection
        db = conn()

        # cusor
        cursor = db.cursor()

        # SQL
        sql = "insert into guestbook values(null,%s,%s,%s,now())"
        count = cursor.execute(sql,(name,password,message))

        # commit
        db.commit()

        #
        cursor.close()
        db.close()

        #
        return count == 1

    except OperationalError as e:
        print(f'error : {e}')


def deleteby_no_and_password(no,password):
    try:
        # connection
        db = conn()

        # cusor
        cursor = db.cursor()

        # SQL
        sql = "delete from guestbook where no=%s and password=%s"
        count = cursor.execute(sql, (no,password))

        # commit
        db.commit()

        #
        cursor.close()
        db.close()

        #
        return count == 1

    except OperationalError as e:
        print(f'error : {e}')

def conn():
    return connect(user='webdb',
                     password='webdb',
                     host='localhost',
                     port=3306,
                     db='webdb',
                     charset='utf8')