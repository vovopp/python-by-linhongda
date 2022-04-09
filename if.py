# if判斷句

#1
from logging import fatal


hungry = True
if hungry:
    print("我就去吃飯") 

#2    
rainy = True
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班")

#3
score = 100
if score==100:
    print("我給你1000元")
elif score>=80:
    print("我給你500元")
elif score>=60:
    print("我給你100元")
else:
    print("你給我300元")

#4
score = 100
rainy = True
if score==100 and rainy:
    print("我給你1000元")
else:
    print("你給我100元")

#5
score = 100
rainy = True
if score==100 or rainy:
    print("我給你1000元")
else:
    print("你給我100元")

#6
score = 90
rainy =False
if score==100 or not(rainy):
    print("我給你1000元")
else:
    print("你給我100元")


def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(3,4,5))


