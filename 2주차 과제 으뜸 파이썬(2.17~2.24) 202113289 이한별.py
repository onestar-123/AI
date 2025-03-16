#2.17
print(2, 2<<1, 2<<2, 2<<3, 2<<4, 2<<5, 2<<6, 2<<7, 2<<8, 2<<9)

#2.18
n=int(input('정수를 입력하세요: '))
if n%2==0:
    print('이 수가 짝수인가요?',bool(1))
else:
    print('이 수가 짝수인가요?',bool(0))
    
#2.19
n=int(input('정수를 입력하세요 :'))
if n>=0 and n<=100 and n%2==0:
    print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?',bool(1))
else:
    print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요?',bool(0))

#2.20
print(bin(5),'&',bin(6),'=',bin(5&6))
print(bin(5),'|',bin(6),'=',bin(5|6))
print(bin(5),'^',bin(6),'=',bin(5^6))

#2.21
n=int(input('정수를 입력하시오 : '))
print(n,'의 2진수 값:', bin(n))
print(n,'의 2진수 값에 대한 비트단위 부정값 :', bin(~n))

#2.22
a=int(input('정수 a를 입력하시오 :'))
b=int(input('정수 b를 입력하시오 :'))
print('a / b의 몫 :',a//b)
print('a / b의 나머지 :',a%b)

#2.23
n=int(input('세 자리 정수를 입력하시오 :'))
print('백의 자리 :',n//100)
print('십의 자리 :',(n%100)//10)
print('일의 자리 :',n%10)

#2.24
n=int(input('세 자리 정수를 입력하시오 :'))
print('일의 자리 :',n%10)
print('십의 자리 :',(n%100)//10)
print('백의 자리 :',n//100)
