#LAB 7-1
import datetime as dt
today = dt.date.today()
print("오늘의 날짜 : {}년 {}월 {}일".format(today.year, today.month, today.day))
Today = dt.datetime.now()
if Today.hour > 12:
    print("현재시간 : 오후 {}시 {}분 {}초".format(Today.hour - 12, Today.minute, Today. second))
elif Today.hour ==12:
    print("현재시간 : {}시 {}분 {}초".format(Today.hour, Today.minute, Today. second))
else:
    print("현재시간 : 오전 {}시 {}분 {}초".format(Today.hour, Today.minute, Today. second))

#LAB 7-2-1
print("\n")
import datetime as dt
today = dt.date.today()
print("오늘은  {}년 {}월 {}일 입니다.".format(today.year, today.month, today.day))
xMas = dt.datetime(2025, 12, 25)
time_gap = xMas - dt.datetime.now()
print("다음 크리스마스 까지는 {}일 {}시간 남았습니다.".format(time_gap.days, time_gap.seconds//3600))

#LAB 7-2-2
print("\n")
import datetime as dt
today = dt.date.today()
print("오늘은  {}년 {}월 {}일 입니다.".format(today.year, today.month, today.day))
first_2036 = dt.datetime(2036, 1, 1)
time_gap = first_2036 - dt.datetime.now()
print("2036년 새해 까지는 {}일 {}시간 남았습니다.".format(time_gap.days, time_gap.seconds//3600))

#LAB 7-2-3
print("\n")
import datetime as dt
today = dt.date.today()
print("오늘은  {}년 {}월 {}일 입니다.".format(today.year, today.month, today.day))
next_BD = dt.datetime(2026, 6, 10)
time_gap = next_BD - dt.datetime.now()
print("다음 생일 까지는 {}일 {}시간 남았습니다.".format(time_gap.days, time_gap.seconds//3600))

#LAB 7-3-1
print("\n")
import datetime as dt
t=dt.timedelta(days=1000)
plus1000day = dt.datetime.now() + t
print("1000일 후 =", plus1000day)
'''
#LAB 7-3-2
print("\n")
import datetime as dt
f_year, f_month, f_day = map(int,input("처음으로 사귄 연도와 월, 일을 입력하시오 : ").split())
t=dt.timedelta(days=100)
plus100day= dt.datetime(f_year, f_month, f_day) + t
print("100일 기념일은 : {}년 {}월 {}일 입니다.".format(plus100day.year, plus100day.month, plus100day.day))
'''
#LAB 7-4-1
print("\n")
import math as m
for i in range(2,11):
    print("4**{} = {:>10}".format(i, m.pow(4, i)))
    
#LAB 7-4-2
print("\n")
import math as m
for i in range(0,181,10):
    print("{}degree = {}radian".format(i, m.radians(i)))
    
#LAB 7-4-3
print("\n")
import math as m
for i in range(0,181,10):
    print("sin({}) = {}".format(i, m.sin(m.radians(i))))

#LAB 7-5-1
print("\n")
import random as rd
print("0에서 100 이하의 정수 중에서 5의 배수")
r_list=[]
for i in range(3):
    r_list.append(rd.randrange(5,101,5))
print(r_list)

#LAB 7-5-2
print("\n")
n_list = list(range(1,11))
print("0에서 10 사이의 임의의 정수 :", rd.sample(n_list, 3))
'''
#LAB 7-7-1
print("\n")
import turtle as t
t.shape("turtle")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.done

#LAB 7-7-2
print("\n")
import turtle as t
t.shape("turtle")
n=0
for i in range (2):
    n+=100
    for _ in range(3):
        t.forward(n)
        t.left(120)
t.done

#LAB 7-7-3
print("\n")
import turtle as t
t.shape("turtle")
n=0
for i in range (3):
    n+=100
    for _ in range(3):
        t.forward(n)
        t.left(120)
t.done

#LAB 7-7-4
print("\n")
import turtle as t
t.shape("turtle")
for _ in range(4):
    t.forward(100)
    t.left(90)
t.done
'''
#LAB 8-1-1
#a = [10, 20, 30]
#print(a[3])
#IndexError: list index out of range

#n= int('20%')
#ValueError: invalid literal for int() with base 10: '20%'

#a = 100 +'200'
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

#LAB 8-1-2
print("\n")
try:
    a = [10, 20, 30]
    print(a[3])
except Exception as e:
    print('error :', e)
    
try:
    n= int('20%')
except Exception as e:
    print('error :', e)

try:
   a = 100 +'200'
except Exception as e:
    print('error :', e)

#LAB 8-2
print("\n")
try:
    10*(30/0)
except ZeroDivisionError:
    print("오류 : 0으로 나눔을 시도했습니다.")
'''
try:
    x = int(input('정수 x를 입력하세요: '))
except ValueError:
    print("오류 : 입력 값이 정수가 아닙니다.")
except:
    print("오류 : 정수를 입력하세요.")    


#LAB 8-2
print("\n")
a = [1, 2, 3, 4, 5]
try:
    A=int(input("a의 요소를 하나 선택하세요:"))
    if A == 1:
        B = '첫'
    if A == 2:
        B = '두'
    if A == 3:
        B = '세'
    if A == 4:
        B = '네'
    if A == 5:
        B = '다섯'
    print(A,"은(는)", B,"번 째 요소 입니다.")
except ValueError:
    print("오류 : 입력값이 정수나 실수가 아님") 
'''
