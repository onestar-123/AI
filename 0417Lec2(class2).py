class Student:
#초기화 함수는 __init__ 정해짐, 규칙
    def __init__(self, name, score):
        self.__name=name
        self.__score=score

    def __str__(self):
        return '이름: {}, 점수: {}'.format(self.__name, self.__score)
        
    def get_grade(self):
        if self.__score >= 90:
            return "A"
        elif self.__score >=80:
            return "B"
            

민수 = Student("민수", 85)
지영 = Student("지영", 92)
print(민수.get_grade())
print(지영.get_grade())

#class 호출해서 돌아가는 동안 민수 = self
#slef.name = 민수.name = name/ 민수.score = score

print(민수)
#print(민수.__name)
