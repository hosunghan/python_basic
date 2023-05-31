#section02-1
#파이썬 기초 코딩
#print 구문의 이해
#기본 출력
print("Hello Python!")
print('Hello Python!')
print("""Hello python!""")
print('''Hello python!''')
#Separator옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019','02','19', sep='-')
print('niceman', 'google.com', sep='@')
#end 옵션 사용
print('Welcom To', end=' ')
print('the black parade', end=' ')
print('piano notes')
#format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{a} and {b}'.format(a='You', b='Me'))
# %s : 문자, $d : 정수, %f : 실수
print("%s's favorite number is %d" %('hosung', 7))
print("Test1 : %5d, Price:  %4.2f" %(776, 6543.123))
print("Test1 : {0: 5d}, Price: {1: 4.2f}".format(776, 6543.123))
print("Test1 : {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6543.123))
"""
참고 : Escape 코드
\n :개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
....
"""
print("'you")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\')
print('\\you\\\n\n\n\n\n\n')
print('\t\t\ttest')

# Secton02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습
# import this
import sys
# 파이썬 기본 인코딩
print(sys.stdin.encoding)
print(sys.stdout.encoding)
# 출력문
print('My name is Goodboy!!')
# 변수 선언
myName = 'Goodboy'
# 조건문
if myName == 'Goodboy':
    print("Ok")
# 반목분
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i,j), i*j)
# 변수 선언(한글)
이름 = "좋은 사람"
print(이름)
# 함수 선언
def 인사():
    print("안녕하세요, 반갑습니다.")
인사()
# 클래스
class Cookie:
    pass
# 객체 생성
cookie = Cookie()
print(id(cookie))
print(dir(cookie))