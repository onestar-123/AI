class Phone:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery
        
#사용시간 - 배터리 줄이기
    def use(self, minutes):
        self.battery -= 0.5*minutes
        print("배터리 잔량은", self.battery, "입니다.")
        
#충전시간 - 배터리 올리기        
    def charge(self, minutes):
        self.battery += minutes
        print("배터리 잔량은", self.battery, "입니다.")
        
my_phone = Phone("Galaxy", 80)

'''
my_phone,brand = "Galaxy"
my_phone.battery = 80
'''

my_phone.use(30)
my_phone.charge(20)




