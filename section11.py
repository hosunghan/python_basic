#파이썬 외부 파일 처리
#파이선 Excel, CSV파일 읽기 및 쓰기

#CSV : MIME- text/csv

#구분자가 ,
import csv
import encodings
with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader=csv.reader(f)
    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()
    for c in reader:
        print(c)

print()
print()

#구분자가 | 일때,
with open('./resource/sample2.csv', 'r', encoding='euc-kr') as f:
    reader=csv.reader(f, delimiter='|')
    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()
    for c in reader:
        print(c)

print()
print()

with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader=csv.DictReader(f)

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print('-----------------')


print()
print()


#파일 쓰기
w=[[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]]
#라인별로 쓰기 : 라인별로 검수해서 쓰기
with open('./resource/sample3.csv', 'w') as f:
    wt=csv.writer(f)

    for v in w:
        wt.writerow(v)

#리스트 전체로 한번에 쓰기
#검수가 끝나서 한번에 쓰기
with open('./resource/sample4.csv', 'w') as f:
    wt=csv.writer(f)
    wt.writerows(w)


#XSL, XLSX
#openpyxl, xlswriter, xlrd, xlwt, xlutils 등
#주로 pandas를 사용함(openpyxl, xlrd)
#pip install xlrd
#pip install openpyxl
#pip install pandas


import pandas as pd

# sheetname='시트명', 또는 숫자, header=숫자, skiprow=숫자 등
xlsx = pd.read_excel('./resource/sample.xlsx', engine='openpyxl')

#상위 데이터 확인
print(xlsx.head())
print()


#데이터 확인
print(xlsx.shape) #행, 열 확인

#엑셀, csv다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)

