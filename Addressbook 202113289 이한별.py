import json
addressbook={}
with open("addressbook.json","r",encoding="utf-8") as f:
    addressbook = json.load(f)
    
print("수정 전 주소록", addressbook)

name = None
while (True):
    name = input("실행할 작업을 선택하세요(추가/삭제/검색/점검/저장): ")
    
    if (name=="저장"):
        break
    
    if (name=="추가"):
        name = input("추가할 이름을 입력하세요: ")
        phoneNum = input("전화번호를 입력하세요: ")
        addressbook[name] = phoneNum
    
    if (name=="삭제"):
        name=input("삭제할 이름을 입력하세요:")
        del addressbook[name]
    
    if (name=="검색"):
        name = input("검색할 이름을 입력하세요: ")
        if name in addressbook:
            print(name, "번호는", addressbook[name],"입니다.")
        else:
            print(name, "은(는) 주소록에 없습니다.")

    if (name=="점검"):
        addressbook=dict(sorted(addressbook.items()))
        print("현재 주소록", addressbook)
        
addressbook=dict(sorted(addressbook.items()))

with open("addressbook.json","w", encoding="utf-8") as f:
    json.dump(addressbook, f, ensure_ascii=False, indent=4)
print("주소록이 저장되었습니다.")
print("수정 후 주소록", addressbook)
