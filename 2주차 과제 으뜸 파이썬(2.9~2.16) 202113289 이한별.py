#2.9
print('섭씨 화씨')
celsius=0
fahrenheit=(9/5)*celsius+32
while celsius<=50:
    print(celsius,' ',fahrenheit)
    celsius+=10
    fahrenheit=(9/5)*celsius+32
#2.10
celsius=int(input('섭씨 온도를 입력하세요 :'))
fahrenheit=(9/5)*celsius+32
print('섭씨',celsius,'도는 화씨',fahrenheit,'도 입니다.')

#2.11
fahrenheit=int(input('화씨 온도를 입력하세요 :'))
celsius=(5/9)*(fahrenheit-32)
print('화씨',fahrenheit,'도는 섭씨',celsius,'도 입니다.')

#2.12
radius=11
PI=3.141592
print('원의 반지름 =',radius)
print('원의 둘레 =', 2*PI*radius)
print('원의 면적 =',PI*radius**2)

#2.13
radius=int(input('원의 반지름을 입력하세요 :'))
print('원의 둘레 =', 2*PI*radius,'원의 면적 =',PI*radius**2)

#2.14 sqrt_table.py
n=2
while n<=10:
    print(n,'의 제곱근 =',n**(1/2))
    n+=1

#2.15
a=int(input('밑변을 입력하세요 :'))
b=int(input('높이를 입력하세요 :'))
print('빗변 :',(a**2+b**2)**(1/2))

#2.16-(1)
print('회전하기 전 :',(1+2j))
print('90도 회전한 후 :',(1+2j)*(0+1j))

#2.16-(2)
print('회전하기 전 :',(1+2j))
cos30=(1/2)*(3**(1/2))
print('30도 회전한 후 :',(1+2j)*(cos30+0.5j))
