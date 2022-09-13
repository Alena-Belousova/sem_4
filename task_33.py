#    Задана натуральная степень k. Сформировать случайным образом список
#  коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
   # Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k= int(input('введите число: '))
a=str()

for stepen in range(0,k+1):
  koeff=random.randint(0, 100)
  
  koeff=str(koeff)
  
  if stepen==0:
    a=a+koeff+'+'
  else:
   
    if stepen==k:
     a=a+koeff+'*x^'+str(stepen)+'=0'
    else:
      a=a+koeff+'*x^'+str(stepen)+'+'
print(a)
  
file = open("C:\\Users\\Alena\\Desktop\\гикбрейнс\\python\\13.09\\task_33.txt", "w")
file.write(a)
file.close()




