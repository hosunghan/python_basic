#파이썬 예외처리의 이해

#예외 종류
#문법적으로 에러가 없지만, 코드 실행(런타임)프세스에서 발ㅇ하는 예외 처리도 중요
#linter : 코드 스타일, 문법 체크

#syntacError : 잘못된 문법
# print("test)
# if True
#     pass

#name Error : 참조 변수 없음
a=10
b=15
#print(c)

# ZeroDivisionError : 0 나누기 에러
#print(10/0)

#IndexError : 인텍스 범위 오버

x=[10,20,30]
# print(x[4])

#KeyError
dic={
    'name' : 'kim',
    'age':33,
    'city':'seoul'
}

# print(dic['hobby'])
print(dic.get('hobby'))

#AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시 예외
from cgi import print_arguments
from cmath import exp
import time

from matplotlib.font_manager import FontProperties
print(time.time())
# print(time.month())

#ValueError : 참조 값이 없을 때 발생
x=[1,3,6]
# x.remove(10)
# x.index(10)

#FileNotFoundError
# f=open('test.txt', 'r') #예외 발생

#TypeError
x=[1,3]
y=(1.2)
z='test'

#print(x+y) #예외
#print(x+x)
#print(x+list(y)) #예외

#항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
#그 후 런타임 예외 발생 시 에외 처리 코딩 권장(EAFP 코딩 스타일)

#예외 처리 기본
#try : 에러가 발생할 가능성이 있는 코드 실행
#except : 에러명1
#except : 에러명2
#else :에러가 발생하지 않았을 경우 실행
#finally:항상 실행

name=['kim', 'lee', 'Park']
try:
    z='kim'
    x=name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not Found it - Occurred ValueError')
else:
    print('OK! else!')

print()
print()

try:
    z='jin'
    x=name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not Found it - Occurred ValueError')
else:
    print('OK! else!')

print()
print()

try:
    z='kim'
    x=name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except:
    print('Not Found it - Occurred ValueError')
else:
    print('OK! else!')
finally:
    print('finally OK!')

print()
print()

#예외처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print('finally OK')

print()
print()

try:
    z='kim'
    x=name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:#순서가 중요함
    print('Not Found it - Occurred ValueError')
except IndexError:
    print('Not Found it - Occurred IndexError')
except Exception:#이것도 저것도 아니면 Exception이 잡음
    print('Not Found it - Occurred Exception')
else:
    print('OK! else!')
finally:
    print('finally OK!')

print()
print()
#예외 발생 : raise
#raise 키워드로 예외 직접 발생
try:
    a='33333'
    if a=='kim':
        print('OK 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생')
except Exception as f:
    print(f)
else:
    print('OK!')