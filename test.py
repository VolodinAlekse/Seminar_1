#n = input ('Введите трехзначное число: ' )
#a = int( n[0])
#b = int( n[1])
#c = int( n[2])
#print (' Сумма трехзначного числа: ' , a + b + c )

#S = int(input("Введите общее количество журавликов: "))
#if not S % 6:
 #    x = S // 6
  #   print(f'Катя {x * 4} ')
   #  print(f'Сережа {x} ')
    # print(f'Петя {x}') 

#S = int(input('Введите сколько всего ребята сделали журавликов? : '))
#ps = int(str(S)) // 6
#print ('Петя и Сережа сделали по' , ps, ', а Катя сделала ' , ps*4 )

#Задача_3вар_1
#n = int(input('Введите номер билета для проверки '))
#if n > 999999 or n < 0:
 #   print('Номер билета введен неправильно!')
#else:
 #   i = 0
  #  sum1 = 0
   # sum2 = 0
    #while i < 6:
     #   if i < 3:
      #      a = n % 10
       #     n = n // 10
        #    sum1 += a
         #   i += 1
        #else:
         #   a = n % 10
          #  n = n // 10
           # sum2 += a
            #i += 1
    #if sum1 == sum2:
     #   print('Вам повезло, Ваш билет счастливый!')
    #else:
     #   print('В этот раз не повезло')

#Задача_3Вар_2?

#while True :
 #   number = input('Введите номер билета (шесть цифр) : ')
  #  if number. isdigit() and len(number) == 6:
   #     if sum(map(int, number[:3])) == sum(map(int, number[3:] )):
    #     print('Да, Билет Счастливый:)! ') 
    #else:
     #   print(' Извините, это обычный билет:(! )')
#else:
 #  print('Билет введен неверно, попробуйте еще раз. ')

#Задача_3Вар_3

#t = input('Введите номер билета (шесть цифр): ')
#if int(t[0]) + int(t[1]) + int(t[2]) == int(t[3]) + int(t[4]) + int(t[5]):
#    print('Да - Это счастливый билет:)! ')
#else:
#    print('Нет - Это обычный билет :(! ')

#Задача_4Вар_1

n = int(input('Введите число долек длины шоколадки '))
m = int(input('Введите число долек ширины шоколадки '))
k = int(input('Сколько долек вы хотите отломить? '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Да, можно осуществить один разлом по прямой')
else:
    print('Разлом только по одной прямой невозможен')