class Television:
    serialNumber = 0
    def __init__(self):
        Television.serialNumber +=1
        self.number = Television.serialNumber
        
    def __str__(self):
        return '{}'.format(self.number)

    
t1 = Television()
t2 = Television()
my_tv = Television()


print(t1, t2, my_tv)
