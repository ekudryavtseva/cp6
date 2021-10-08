try:
 N=int(input('Введите количество элементов массива array:'))
 a=[]
 for i in range(N):
   a.append(int(input('Введите элемент массива array:')))
 delta=int(input('Введите delta:'))
 min=a[0]
 for i in range(N):
   if a[i]<min:
    min=a[i]
 counter=0
 for i in range(len(a)):
   if min+delta==a[i]:
    counter+=1
 print (counter)
except ValueError:
 print('Ошибка. Введите число')