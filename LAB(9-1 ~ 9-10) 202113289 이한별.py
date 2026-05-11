#LAB 9-1
print((200).__sub__(100))
print((200).__mul__(100))
print((200).__truediv__(100))
print([10,20,30,40].pop())
print('리스트가 호출할 수 없는 메소드는 2) keys()')
'''
print(dir(int))
print(dir(list))
'''

#LAB 9-2
'''
print('\n')
print('객체 지향 프로그래밍 = 컴퓨터가 수행하는 작업을 객체들 사이의 상호작용으로 표현하는 것')
print('절차적 프로그래밍 = 함수나 모듈을 만들어두고 이것들을 문제해결 순서에 맞게 호출하여 수행하는 방식')
print('그래픽 사용자 인터페이스 = 아이콘·버튼·메뉴 같은 시각적 요소를 통해 사용자가 컴퓨터나 전자 기기와 상호작용하는 방식')
print('절차적 프로그밍은 만들어 둔 함수의 호출을 통해 실행, 객체 지향 프로그래밍은 잘 짜여진 클래스를 통해 객체를 만들어 실행')
'''

#LAB 9-3
'''
print('\n')
print('클래스 = 프로그램 상에서 사용되는 속성과 행위를 모아놓은 집합체')
print('객체 = 속성과 메소드를 가진 요소')
print('인스턴스 = 클래스로부터 만들어지는 각각의 개별적인 객체')
print('클래스의 속성 = 객체의 정보')
print('클래스의 동작 = 함수(메소드)를 통한 실행 또는 행동')
'''

#LAB 9-4
print('\n')
class Dog:
    def bark(self):
        print('멍멍~~')
my_dog = Dog()
my_dog.bark()

#LAB 9-5
print('\n')
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print('멍멍~~')
my_dog = Dog('Jindo')
my_dog.bark()

#LAB 9-6
print('\n')
class Dog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Dog(name = '+self.name+')'
my_dog = Dog('Jindo')
print('my_dog의 정보 :', my_dog)


#LAB 9-7
print('\n')
n = 100
m = 100
if n is m:
    print('n is m')
else:
    print('n is not m')
''' n, m 이라는 서로 값이 같은 정수형 인스턴스 변수에 대해 is 연산자가 Ture를 반환했기 때문에  n is m이 출력된다.'''

#LAB 9-8
print('\n')
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector2D(self.x* other.x, self.y * other.y)
    
    def __truediv__(self, other):
        return Vector2D(self.x/other.x, self.y/other.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __str__(self):
        return "({}, {})".format(self.x,self.y)

v1=Vector2D(30,40)
v2=Vector2D(10,20)
print('v1 * v2 = ', v1*v2)
print('v1 / v2 = ', v1/v2)
v1=Vector2D(10,20)
print('-v1 = ', -v1)

#LAB 9-9
print('\n')
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __lt__(self, other):
        if self.x**2 + self.y**2 < other.x**2 +other.y**2:
            return True
        else:
            return False
    def __le__(self, other):
        if self.x**2 + self.y**2 <= other.x**2 +other.y**2:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.x**2 + self.y**2 > other.x**2 +other.y**2:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.x**2 + self.y**2 >= other.x**2 +other.y**2:
            return True
        else:
            return False
        
    def __str__(self):
        return "({}, {})".format(self.x,self.y)
v1 = Vector2D(30,40)
v2 = Vector2D(10,20)
print('v1 > v2 = ', v1 > v2)
print('v1 >= v2 = ', v1 >= v2)
print('v1 < v2 = ', v1 < v2)
print('v1 <= v2 = ', v1 <= v2)

#LAB 9-10
print('\n')
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
r1 = Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['width'])

class Rect:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
r1 = Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['_Rect__width'])
