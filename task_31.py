#    Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math
numb= int(input('введите число '))
def funk(numb):
    while numb % 2 == 0:
      print (2),
      numb = numb / 2

      for i in range(3,int(math.sqrt(numb))+1,2):
          while (numb % i == 0):
            print (i)
            numb = numb / i
   
      if numb > 2:
        print(numb)
funk(numb)




