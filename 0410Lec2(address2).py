import json

#import는 다른사람이 짜놓은 것 불러옴 / json은 파일 오픈 저장 기능 있음
# 주소록 데이터
addressbook = dict()
name = None
while (True):
    name = input("이름을 입력하세요: ")
    if (name=="끝"):
        break
    phoneNum = input("전화번호를 입력하세요: ")

    addressbook[name] = phoneNum

# 1. 파일로 저장
with open("addressbook.json","w", encoding="utf-8") as f:
    json.dump(addressbook, f, ensure_ascii=False, indent=4)
print("주소록이 저장되었습니다.")


'''
#with open -> 하드디스크에 방을 하나 만들어, json.dump는 파일에 addressbook을 저장

# 2. 파일에서 다시 불러오기
with open("addressbook.json","r",encoding="utf-8") as f:
    addressbook = json.load(f)

print("불러온 주소록:", addressbook)
print("김영호 번호:", addressbook["김영호"])
'''


#과제 : 새로 작업  할 시 기존 파일 불러와서 추가하는것
#+a => 탐색 등의 새로운 작업, 기존 멤버 삭제 등
