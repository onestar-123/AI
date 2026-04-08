'''
set1={0,1,2,2,4,5,5}
print(set1)
set2={0,5,2,2,4,1}
print(set2)
'''
aSet={1,2,3,4}
bSet={2,4,6,7}

cSet=aSet-bSet
cSet=aSet.difference(bSet)

#cSet=aSet&bSet
#cSet=aSet.intersection(bSet)
'''
cSet= aSet | bSet
cSet=aSet.union(bSet)
'''
print(cSet)
