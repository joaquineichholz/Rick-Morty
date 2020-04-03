import re


s = 'hola'
t = ['1 hola como estas', '2 chao hola chao', '3 aassa hola', '4 ola', '5 nada', '6 nhola']

for x in t:
    if re.search(s, x):
        print(x)