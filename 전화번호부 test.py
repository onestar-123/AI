page={}
print('입력을 마치려면 이름에 0을 입력하세요')
while 1>0:
    name=input('이름을 입력하세요: ')
    if name=='0':
        break
    
    num=input('번호를 입력하세요: ')
    page[name]=num
print(page)
    
