#LAB 6-1-1
capital_dic = {'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}
print(capital_dic['Korea'])
print(capital_dic['China'])
print(capital_dic['USA'])

#LAB 6-1-2
print("\n")
fruits_dic = {'apple': 5000, 'banana':4000, 'grape': 5300, 'melon':6500}
for fruit in fruits_dic:
    print(fruit, '의 가격은', fruits_dic[fruit], '원 입니다.')

#LAB 6-2
print("\n")
person = {'이름':'홍길동', '나이':26, '몸무게':82}
person['특기'] = '분신술'
print(person)
person['아버지'] = '홍판서'
print(person)
del person['나이']
print(person)

#LAB 6-3
print("\n")
capital_dic = {'Korea':'Seoul', 'China':'Beijing', 'USA':'Washington DC'}
print('Korea' in capital_dic)
print('China' in capital_dic)
print('Indonesia' in capital_dic)
print('Beijing' in capital_dic)

#LAB 6-4
print("\n")
fruits_dic = {'apple': 6000, 'melon':3000, 'banana':5000, 'orange': 7000}
print(fruits_dic.keys())
print(fruits_dic.values())
remove_apple = fruits_dic.pop('apple')
print(fruits_dic)
remove_all = fruits_dic.clear()
print(fruits_dic)

#LAB 6-5-1
print("\n")
fruits_dic = {'apple': 6000, 'melon':3000, 'banana':5000, 'orange': 4000}
fruits_list=list(fruits_dic)
print(fruits_list)
#LAB 6-5-2
fValues_list=list(fruits_dic.values())
print(fValues_list)
#LAB 6-5-3
print('fruits_dic 딕셔너리 항목의 개수 :', len(fruits_dic))
#LAB 6-5-4
list_t=['apple', 'mango']
for name in list_t:
    if name in fruits_dic:
        print(name, 'is in fruits_dic')
    else:
        print(name, 'is not in fruits_dic')
        
#LAB 6-6-1
print("\n")
the_day=(1919, 3, 1)
print(the_day[0],'년', the_day[1], '월', the_day[2], '일은 삼일절 입니다.')
#LAB 6-6-2
list_a=[10, 20, 30]
tuple_a=tuple(list_a)
c,b,a=tuple_a
print('a=', a)
print('b=', b)
print('c=', c)

#LAB 6-7
print("\n")
person = ('홍길동', 2019001, 179)
#person[1]=2019003
person_list = list(person)
person_list[1] = 2020003
person_tuple=tuple(person_list)
print('학번 변동 후 person =', person_tuple)

'''#LAB 6-8-1
print("\n")
x=int(input('x를 입력하세요'))
y=int(input('y를 입력하세요'))
def square(x, y):
    x_sq=x**2
    y_sq=y**2
    return(x_sq, y_sq)
x_sq, y_sq=square(x, y)
print('{} 제곱 = {}, {} 제곱 ={}'.format(x, x_sq, y, y_sq))'''
#LAB 6-8-2
t_a=(10,20,30)
t_b=(40,50,60)
print(t_a+t_b)
#LAB 6-8-3
print('Hello'*3)
print(('Hello',)*3)
#문자열 3개의 반복 -> 하나로 문자열 이룸
#('Hello',)의 반복으로 튜플 구조 이룸

#LAB 6-9-1
print("\n")
lst=['apple', 'mango', 'banana']
s1=set(lst)
print(s1)
#LAB 6-9-2
greet = 'Good afternoon'
s2=set(greet)
print(s2)

#LAB 6-10
print("\n")
S1 ={10, 20, 30, 40}
S2 ={30, 40, 50, 60, 70}
print(S1|S2)
print(S1&S2)
print(S1-S2)
print(S1^S2)
print(S1.issubset(S2))
print(S1.issuperset(S2))
print(S1.isdisjoint(S2))

#LAB 6-11
print("\n")
A = {1, 2}
B = {'A', 'B', 'C'}
def product_set(set1, set2):
    res = set()
    for i in set1:
        for j in set2:
            res = res|{(i,j)}
    return res
AxB= product_set(A,B)
BxA= product_set(B,A)
AxA= product_set(A,A)
BxB= product_set(B,B)
print('AxB =',AxB)
print('BxA =',BxA)
print('AxA =',AxA)
print('BxB =',BxB)

#LAB 6-12
print("\n")
def tuple_sum(tup):
    if isinstance(tup, int):
        return tup
    else:
        accum=0
        for element in tup:
            accum += tuple_sum(element)
    return accum

def product_Set(Set1, Set2):
    Res = set()
    for i in Set1:
        for j in Set2:
            Res=Res|{(i,j)}
    return Res
def exp(input_Set, exponent):
    Res = input_Set
    for _ in range(exponent-1):
        Res = product_Set(Res, input_Set)
    return Res

dice ={1, 2, 3, 4, 5, 6}
cases=exp(dice,3)
over_10 = 0
for c in cases:
    if tuple_sum(c) >=10:
        over_10 +=1
print('주사위를 세 번 던져 발생할 수 있는 사건은', 6**3,'가지 경우가 존재합니다.')
print('주사위를 세 번 던져 나온 눈의 합이 10 이상인 경우는', over_10 ,'가지 입니다.')


for i in range(3,19,1):
    over_n=0
    for n in cases:
        if tuple_sum(n) >=i:
            over_n +=1
    isum=over_n
    print(i, '이상 확률', float(isum/216)*100,'%')
