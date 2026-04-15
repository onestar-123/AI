'''
str3 = input('세 개의 숫자를 입력하세요~').split()
#istr3=int(str3)---> int 함수는 단일 값만 정수로 변환 > 하나씩 해줘야 함
istr3=list(map(int,str3))
print(str3)
'''

#a, b, c = map(int, input('세 개의 숫자를 입력하세요~').split())
#print(a,b,c)
a ='1 2 3'
print(a.split())
