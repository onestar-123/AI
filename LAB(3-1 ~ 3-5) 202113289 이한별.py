#LAB 3-1-1
game_score=int(input("게임 점수를 입력하세요: "))
if game_score >= 1000:
    print("당신은 고수입니다.")
    
#LAB 3-1-2
print("\n")
num_a=int(input("첫 번째 숫자를 입력하세요: "))
num_b=int(input("두 번째 숫자를 입력하세요: "))
if num_a == num_b:
    print("두 값이 일치합니다.")

#LAB 3-2-1
print("\n")
n=int(input("정수를 입력하세요: "))
print("n =", n)
if n % 2 == 0:
    print("n은(는) 짝수 입니다.")

#LAB 3-2-2
print("\n")
x=int(input("정수를 입력하세요: "))
print("x =", x)
if x > 0:
    print("x은(는) 자연수 입니다.")

#LAB 3-3-1
print("\n")
game_score2=int(input("게임 점수를 입력하세요: "))
if game_score2 >= 1000:
    print("고수입니다.")
else:
    print("입문자입니다.")
    
#LAB 3-3-2
print("\n")
num_c=int(input("첫 번째 숫자를 입력하세요: "))
num_d=int(input("두 번째 숫자를 입력하세요: "))
if num_c == num_d:
    print("두 값이 일치합니다.")
if num_c != num_d:
    print("두 값이 일치하지 않습니다.")

#LAB 3-3-3-1
print("\n")
v=int(input("당신은 성인인가요(성인이면 1, 미성년이면 0): "))
if v==1:
    print("당신은 성인입니다.")
else:
    print("당신은 미성년자입니다.")
    
#LAB 3-3-3-2
print("\n")
z=int(input("당신은 성인인가요(성인이면 1, 미성년이면 0): "))
if z==1:
    u=int(input("결혼을 하셨나요(기혼이면 1, 미혼이면 0): "))
    if u==1:
        print("당신은 결혼한 성인입니다.")
    else:
        print("당신은 결혼하지 않은 성인입니다.")
    
else:
    print("당신은 미성년자입니다.")

#LAB 3-4-1
print("\n")
num=int(input("정수를 입력하세요: "))
if num >= 1 and num <= 10:
    print("True")
    
#LAB 3-4-2
print("\n")
age=int(input("나이를 입력하세요: "))
if age > 10 and age < 19:
    print("청소년입니다.")

#LAB 3-5
print("\n")
s=int(input("자동차의 속도를 입력하세요(단위 : km/h ): "))
if s >= 100:
    print("고속")
elif s<100 and s>=60:
    print("중속")
else:
    print("저속")
