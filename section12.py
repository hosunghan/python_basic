#section 12
#python 데이터베이스 연동(sqllite)
#테이블 생성 및 삽입

import imp


import datetime
from queue import PriorityQueue
import sqlite3

#삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDatetime)

#sqllite3
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqite_version', sqlite3.sqlite_version)

#DB생성 & Auto Commit(Rollback)

conn=sqlite3.connect('/Users/hosunghan/workspace/python_basic/resource/database.db', isolation_level=None)

#Cursor
c=conn.cursor()
print('Cursor Type : ', type(c))

#테이블 생성(Data Type ; TEXT, NUMERIC INTEGER REAL BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

#데이터 삽입
# c.execute("INSERT INTO users VALUES(1, 'kim', 'Kim@naver.com', '010-0313-1300', 'kim.com', ?)",(nowDatetime,))
# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", (2, 'park', 'park@daum.net', '010-3115-1355', 'park@com', nowDatetime))

# # # Many 삽입(튜플, 리스트 )
# userList=(
#     (3, 'Lee', 'Lee@naver.com', '010-1231-1344', 'lee.com', nowDatetime),
#     (4, 'Cho', 'Cho@daum.net', '010-1234-1555', 'Cho.com', nowDatetime),
#     (5, 'Yoo', 'Yoo@google.com', '010-5623-1233', 'Yoo.com', nowDatetime)
# )

# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList)

#테이블 삭제
# conn.execute("DELETE FROM users")

# print("user db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level=None 일 경우 자동 반영(오토 커밋)
# conn.rollback() #커밋 하기 전에 롤백
# conn.commit() #커밋 실행

conn.close()

conn=sqlite3.connect('/Users/hosunghan/workspace/python_basic/resource/database.db') #본인 DB 경로
c=conn.cursor()
#테이블 조회(없으면 새로 생성)
c.execute('SELECT * FROM users')

#커서 위치가 변경
# 1개 로우 선택
# print('ONe -> \n', c.fetchone())

# #지정 로우 선택
# print('Three -> \n', c.fetchmany(size=3))

# #전체 로우 선택
# print('All -> \n', c.fetchall())

print()

#순회 1
# rows=c.fetchall()
# for row in rows:
#     print('retrievel > ', row)

#순회2
# for row in c.fetchall():
#     print('retreive2 > ', row)

#순회3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retrieve3 > ', row)

#WHERE Retieve1
param1 = (3,)
c.execute("SELECT * FROM users WHERE id=?", param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) #데이터 없음

print()
print()

#WHERE Retieve2
param2 = 4
c.execute("SELECT * FROM users WHERE id=%s" % param2) # %s, %f, %d
print('param2', c.fetchone())
print('param2', c.fetchall()) #데이터 없음

print()
print()

#WHERE Retieve3
c.execute("SELECT * FROM users WHERE id=:Id", {"Id":5})
print('param3', c.fetchone())
print('param3', c.fetchall()) #데이터 없음

print()
print()

#WHERE Retieve4
param4=(3,5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4', c.fetchall())

print()
print()

#WHERE Retieve5
c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" % (3,4))
print('param5', c.fetchall())

#WHERE Retieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1":2, "id2":5})
print('param6', c.fetchall())

#DUMP 출력
with conn:
    with open('/Users/hosunghan/workspace/python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

#f.close(), conn.close()

#파이썬 데이터 베이스 연동(SQLite)
#테이블 데이터 수정 및 삭제

import sqlite3
#DB생성(파일)
conn=sqlite3.connect('/Users/hosunghan/workspace/python_basic/resource/database.db')

#Cursor 연결
c = conn.cursor()

# #데이터 수정
# c.execute("UPDATE users SET username=? WHERE id=?", ('niceman', 2))
# # conn.commit()

# #데이터 수정2
# c.execute("UPDATE users SET username = :name WHERE id = :id", {'name' : 'goodman', 'id' : 5})
# # conn.commit()

# #데이터 수정3
# c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 3))
# # conn.commit()

#중간 데이터 확인1
for user in c.execute("SELECT * FROM users"):
    print(user)

#Row Delete1
c.execute("DELETE FROM users WHERE id = ?", (2,))
# conn.commit()

#Row Delete2
c.execute("DELETE FROM users WHERE id = :id", {"id" : 5})
# conn.commit()

#Row Delete3
c.execute("DELETE FROM users WHERE id='%s'"%4)
# conn.commit()

print()
print()

for user in c.execute("SELECT * FROM users"):
    print(user)


#테이블 전체 데이터 삭제
print("users db delete : ", conn.execute("DELETE FROM users").rowcount, "rows")

#커밋
conn.commit()

#접속 해제
conn.close()