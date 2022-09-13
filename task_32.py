# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#import numpy as N

ist_inp= input('введите числа через пробел ')
list=[]
list=ist_inp.split(' ')
list=[int (ist_inp) for ist_inp in list] 
print('основной лист: ', list)
dup = [x for i, x in enumerate(list) if x in list[:i]]
print('дубли: ',dup)
list_3=[]
for chislo in list:
    if chislo not in dup:
       list_3.append(chislo)
print(list_3)



