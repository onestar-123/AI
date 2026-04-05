#LAB 3-6-(1)
for _ in range(5):
    print("Hello, Python!")

#LAB 3-6-(2)
for i in range(5):
    print(i)

#LAB 3-7-(1)
print("\n")
n_list=list(range(1,101))
print(n_list)

#LAB 3-7-(2)
print("\n")
n_list=list(range(2,101,2))
print(n_list)

#LAB 3-7-(3)
print("\n")
n_list=list(range(1,101,2))
print(n_list)

#LAB 3-7-(4)
print("\n")
n_list=list(range(-99,0,1))
print(n_list)

#LAB 3-8-(1)
print("\n")
nsum=0
for i in range(1,101):
    nsum+=i
print(nsum)

#LAB 3-8-(2)
print("\n")
nsum=0
for i in range(0,101,2):
    nsum+=i
print(nsum)

#LAB 3-8-(3)
print("\n")
nsum=0
for i in range(1,100,2):
    nsum+=i
print(nsum)

#LAB 3-9
print("\n")
n=7
for i in range(n,-1,-1):
    st=''
    for j in range(i):
        st=st+' '
    print(st+'#')

