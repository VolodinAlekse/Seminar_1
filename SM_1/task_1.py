# Задача №1.
# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input: n = 700 m = 750
# Output: 2

# print('Введите количкство километров, которое машина проедетза день: ')
# n = int(input())
# print('Введите требуемое количество километров: ')
# m = int(input())

# print('Машина проедет', m , 'километров за ', round(m/n+0,5), 'дней')

#n = 700
# = int(input('Введите длину маршрута: '))
#day = (m + n - 1) // n
#print(day)

#Задача №3.
#В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
#За каждой партой может сидеть два учащихся. 
#Известно количество учащихся в каждом из трех классов.
#Выведите наименьшее число парт, которое нужно приобрести для них.
#Input: 20 21 22(ввод чисел НЕ в одну строку)
#Output: 32

print('Введите количество учеников в 1 классе: ')
a = int(input())
print('Введите количество учеников в 2 классе:')
b = int(input())
print('Введите количество учеников в 3 классе:')
c = int(input())

print('Необходимо' , a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2 , ' парт ')