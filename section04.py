# 파이썬 데이터 타입(자료형)
#리스트, 튜플
#리스트(순서O, 중복O, 수정O, 삭제O)

from cgi import print_arguments


a = []
b = list()
c = [1,2,3,4]
d = [10,100, 'Pen', 'Banana', 'Ornage']
e = [10, 100, ['Pen', 'Banana', 'Oange']]

#indexing
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])



#슬라이싱
print(d[0:3])
print(e[2][1:3])

#연산
print(c + d)
print(c*3)
print(str(c[0])+'hi')

#리스트 수정, 삭제
c[0]=77
print(c)

c[1:2] = [100,200,1000]
print(c)
c[1] =  ['a', 'b', 'c']
print(c)


del c[1]
print(c)
del c[-1]
print(c)


print()
print()
print()

#리스트 함수
y = [5,3,2,1,5]
y.append(6)
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7)
print(y)
y.remove(2)
print(y)
y.pop()
print(y)
ex = [88,77]
y.extend(ex)
print(y)
y.append(ex)
print(y)



#삭제 : del, remove, pop



# 튜플 (순서 O, 중복 O, 수정 X, 삭제 X)
a = ()
b = (1,)
c = (1,2,3,4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

print(c+d)
print(c*3)

#튜플 함수
z = (5,2,1,3,5)
print(z)
print(3 in z)
print(z.index(3))
print(z.count(1))

print()
print()
print()

# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서X, 중복X, 수정O, 삭제O

#Key, Value(JSon) -> MongoDB
#선언
a = {'name' : 'Kim', 
     'Phone' : '010-9321-1231', 
     'birth' : 713012}

b = {0: 'Hello python',
     1: 'Hello Coding'}

c = {'arr' : [1,2,3,4,5]}

print(type(a))

#출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3])

#딕셔너리 추가
a['address'] = 'Soeul'
print(a)
a['rank'] = [1,2,3,4]
a['rank2'] = (1,2,3)
print(a)



# keys, values, items
print(a.keys())
print(list(a.keys()))

temp=list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

print(3 in b)

print()
print()
print()

# 집합(set) (순서X, 중복X)
a = set()
b = set([1,2,3,4])
c = set([1,2,3,4,5,6])

print(type(a))
print(c)
t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1,2,3,4,5,6])
s2 = set([5,6,7,8,9,10])

print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7,8,10,15])
s3.add(18)

print(s3)
s3.add(7)
print(s3)

s3.remove(15)
print(s3)
type(s3)
