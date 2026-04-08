person ={'이름' : '홍길동', '나이' : 26, '몸무게' : 82}
for key in person:
    print('{}:{}'.format(key, person[key]))
        

print(person['이름'])
print(person['나이'])
print(person['몸무게'])
person['국적']='대한민국]'
print(person)
print(type(person.keys()))

'''
students = {2019001:'이순신', 2019002:'김유신', 2019003:'강감찬'}
print(students[2019001])
print(students[2019002])
print(students[2019003])
'''
