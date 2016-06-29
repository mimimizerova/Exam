#Мизерова Катя, экзамен
f = open('exam.txt', 'r',encoding='utf-8')
a = f.read()
import re
reg=re.compile('([А-Я]\.[А-Я]?\.?|[А-Я][а-я]+)( [А-Я][а-я]+)')
m=re.findall(reg, a)
s=''
for element in m:
    for word in element:
        s+=word
    print (s)
    s=''
f.close()

