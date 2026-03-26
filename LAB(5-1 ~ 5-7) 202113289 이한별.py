#LAB 5-1-1
even_list = [2, 4, 6, 8, 10]
print(even_list)

#LAB 5-1-2
print("\n")
evenList=list(range(2,11,2))
print(evenList)

#LAB 5-1-3
print("\n")
nations = ['Korea', 'China', 'India', 'Nepal']
print(nations)

#LAB 5-1-4
print("\n")
friends = ['길동', '철수', '은지', '지은', '영민']
print(friends)

#LAB 5-1-5
print("\n")
stirng=list('XYZ')
print(stirng)

#LAB 5-2-(1,2,3)
print("\n")
prime_list =[2, 3, 5, 7]
print(prime_list)
print('prime_list의 첫 원소 :', prime_list[0])
print('prime_list의 마지막  원소 :', prime_list[3])
print('prime_list의 마지막  원소 :', prime_list[-1])

#LAB 5-2-(4,5,6)
print("\n")
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print(nations)
print('nations의 첫 원소 :', nations[0])
print('nations의 마지막  원소 :', nations[-1])
print('nations의 마지막  원소 :', nations[len(nations)-1])

#LAB 5-3-(1,2)
print("\n")
prime_list =[2, 3, 5, 7]
print('소수 목록 :',prime_list)
prime_list.append(11)
print('추가 후 소수 목록 :', prime_list)
print('삭제 전 소수 목록 :', prime_list)
prime_list.remove(3)
print('삭제 후 소수 목록 :', prime_list)

#LAB 5-3-(3,4)
print("\n")
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('국가 목록 :',nations)
nations.append('Nepal')
print('추가 후 국가 목록 :', nations)
if 'Japan' in nations:
    print('Japan은(는) 국가 목록에 있습니다.')
else:
    print('Japan은(는) 국가 목록에 없습니다.')
if 'Russia' in nations:
    print('Russia은(는) 국가 목록에 있습니다.')
else:
    print('Russia은(는) 국가 목록에 없습니다.')

#LAB 5-4-1
print("\n")
prime_list =[2, 3, 5, 7]
print('1에서 10까지의 소수 :', prime_list)
print('최솟값 :', min(prime_list))
print('최댓값 :', max(prime_list))
print('합계 :', sum(prime_list))
print('평균 :', sum(prime_list)/len(prime_list))

#LAB 5-4-2
print("\n")
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('국가 목록 :',nations)
print('사전에 가장 먼저 나오는 나라 :', min(nations))
print('사전에 가장 뒤에 나오는 나라 :', max(nations))

#LAB 5-5-1
print("\n")
a = [1, 2, 3]
b = [10, 20, 30]
a.append(b)
print(a)
a = [1, 2, 3]
b = [10, 20, 30]
a.extend(b)
print(a)

#LAB 5-5-(2,3,4,5)
print("\n")
nlist = list(range(1,11))
print('nlist =', nlist)
nlist.insert(0, 0)
print('nlist =', nlist)
nlist.reverse()
print('nlist =', nlist)
final=nlist.pop()
print('마지막 원소 =',final)
print('nlist =', nlist)

#LAB 5-6
print("\n")
n=int(input('반복할 정수를 입력하시오 :'))
list1=[1,2,3]
list2=n*list1
print(list2)

#LAB 5-7
print("\n")
n_list=list(range(15))
print('n_list =', n_list)
print('s_list1 =', n_list[0:5])
print('s_list2 =', n_list[6:11])
print('s_list3 =', n_list[11:])
print('s_list4 =', n_list[2:11:2])
print('s_list5 =', n_list[10:5:-1])
print('s_list6 =', n_list[10:1:-2])


