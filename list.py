'''
score=[87,84,95,67,88,94,63]
names = ["영호", "순자", "영식", "순희", score]
addressbook=[["영호", 25, "010-0000-0000"],["철수", 30, "010-1111-1111"]]
for i in addressbook:
    print(i)
    print(type(i))

ri=list(range(5))
print(ri)
print(ri[0:3])

myString = "apple"

for ch in myString:
    print(ch)

    
listString = list(myString)
print(listString)

n_list =[10, 20, 30, 40]
n_list.append(50)
print(n_list)

n_list=[11, 22, 33, 44, 55, 66]
print(n_list)

n_list.remove(44)
print(n_list)

n_list=[11, 22, 33, 44, 55, 66]
a=n_list.pop()
print(a)
print(n_list)


a_list = [10, 20, 30, 40]
print(10 in a_list)
print(50 in a_list)


list1=[20, 10, 40, 50, 30]
list2=sorted(list1)
print(list1)
print(list2)
'''
list1=[1,2,3,4]
list2=[1,2,4,3]
print(list1<list2)
