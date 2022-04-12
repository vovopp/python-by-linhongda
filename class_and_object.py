class phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof
    
    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False    

    def add(self,number1,number2):
        return number1 + number2

phone1 = phone("ios",123,True)   
print(phone1.add(5,6))