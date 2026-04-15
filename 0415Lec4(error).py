'''
try:
    a=1/0
except:
    print("0으로 나누지 마세요!!")
'''
while(True):
    try:
#        a, b = input('두 수를 입력하시오: ').split()
#       result = int(a)/int(b)
        a, b = map(int,input('두 수를 입력하시오: ').split(','))
        #map(int,['1','2']) int를 순서대로 적용
        print('{}/{}={}'.format(a,b,result))
        break
    except:
        print('두 수가 정확한지 확인하세요.')
