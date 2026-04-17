student1 = {"name":"민수", "score":85}
student2 = {"name":"지영", "score":92}

def get_grade(student):
    if student["score"]>=90:
        return "A"
    elif student["score"]>=80:
        return "B"
    else:
        return "C"
print(get_grade(student1))
print(get_grade(student2))

#학생 많아지면 위의 방법 불편
