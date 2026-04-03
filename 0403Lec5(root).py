'''
def root(a,b,c):
    if (b**2.0-4.0*a*c)<0:
        return None, None
    x1 =(-b+(b**2.0-4.0*a*c)**0.5)/(2.0*a)
    x2 =(-b-(b**2.0-4.0*a*c)**0.5)/(2.0*a)
    return x1, x2
r1,r2 = root(1,2,3)
print(r1,r2)
'''
def print_sum():
    a=1
    b=2
    result = a+b
    print('print_sum() 내부:', a,'과',b,'의 합은', result, '입니다.')
    
a=10
b=20
print_sum()
result= a+b
print(result)
