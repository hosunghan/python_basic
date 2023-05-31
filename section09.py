#파일 읽기/쓰기
#읽기 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a

#파일 읽기
f=open('./resource/review.txt', 'r')
content=f.read()
print(content)
print(dir(f))
#반드시 close 리소스 반환
f.close()

print()
print()

with open('./resource/review.txt', 'r') as f:
    c=f.read()
    print(c)
    print(list(c))
    print(iter(c))


print()
print()

with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print()
print()

with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print('>>>>>>>', content)
    content = f.read()
    print('>>>>>>>', content) # 내용이 없음
    
print()
print()

with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end='##### ')
        line=f.readline()

print()
print()

with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(content)
    for c in contents:
        print(c, end='******')

print()
print()

score=[]
with open('./resource/score.txt', 'r') as f:    
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))

#파일 쓰기
with open('./resource/text1.txt', 'w') as f:
    f.write('Niceman')

with open('./resource/text1.txt', 'a') as f:
    f.write('Goodman')

from random import randint
with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

#writelines: 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['kim', 'park', 'cho']
    f.writelines(list)

with open('./resource/text4.txt', 'w') as f:
    print('Test Content1', file=f)

    





