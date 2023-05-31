#파이썬 흐름제어(제어문)
#조건문 실습

from typing import Tuple


print(type(True))
print(type(False))

if True :
    print('Yes')

if False :
    print('No')

if False :
    print('No')
else:
    print('Yes')

#관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

#참 거짓 종류(True, False)
#참 : '내용', [내용], (내용), {내용}, 1
#거짓 : "", [], (), {}, 0

city = ""
if city:
    print(">>>>True")
else:
    print(">>>>Fasle")


#논리 연산자
#and or not

a=100
b=60
c=15

print('and : ', a>b and b>c)
print('or : ', a>b or c>b)
print('not : ', not a>b )
print(not False)
print(not True)

#산술, 관계, 논리연산자
#산술 > 관계 > 논리 순서로 적용

print('ex1 : ', 5+10 > 0 and not 7 +3 == 10)

score1=90
score2='A'

if score1 >= 90 and score2 =='A':
    print('합격하셨습니다')
else:
    print("불합격입니다.")

#다중조건문
num=90

if num>=90:
    print('num grade A')
elif num>=80:
    print('num grade B')
elif num >=70:
    print('num grade C')
else:
    print('num grade D')

#중첩 조건문
age =27
height=175

if age >= 20:
    if height >= 170:
         print('A possible')
    elif height >=160:
        print('B possible')
    else:
        print('not possible')
else:
    print('other offer possible')

    
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요
# 기본 반복문 : for, while

v1=1
while v1 < 11:
    print('v1 is : ', v1)
    v1+=1

for v2 in range(10):
    print('v2 is : ', v2)

for v3 in range(1,11):
    print('v3 is : ', v3)

# 1~100합
sum1=0
cnt1=0

while cnt1 <=100:
    sum1+=cnt1
    cnt1+=1
print('1~100 : ', sum1)
print('1~100 : ', sum(range(1,101)))
print('1~100 : ', sum(range(1,101,2)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ['kim', 'park', 'cho', 'choi', 'yoo']

for name in names:
    print('your are :', name)

word = 'dreams'
for s in word:
    print('word : ', s)


my_info={
    'name':'kim',
    'age':33,
    'city':'seoul'
}
#기본값은 키
for key in my_info:
    print('my_info', key)
#밸류
for key in my_info.values():
    print('my_info', key)
#키
for key in my_info.keys():
    print('my_info', key)
#아이템
for k, v in my_info.items():
    print('my_info', k, v)

name = 'KennRY'
for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())


# break
numbers = [14,3,5,1,3,56,46,63,36,88]
for num in numbers:
    if num == 56:
        print('found : ', num)
        break
    else:
        print('not found : ', num)


# for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행0)
numbers = [14,3,5,1,3,56,46,63,36,88]
for num in numbers:
    if num == 33:
        print('found : ', num)
        break
    else:
        print('not found : ', num)
else:
    print('Not foune', num)

# continue
lt = ['1', 2,5,True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print('type : ', type(v))


name = 'nice man'
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))









