#Мизерова Катя, экзамен
f = open('exam.txt', 'r',encoding='utf-8')
a = f.read()
import re
reg=re.compile('[А-Я]\. [А-Я][а-я]+')
m=re.findall(reg, a)
for element in m:
    print (element)
f.close()
