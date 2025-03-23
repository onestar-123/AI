a=1
b=1


for i in range(101):
    c=a
    a=b
    b=c+b

    print('{}th Pib. Number is {}'.format(i+2, b))
