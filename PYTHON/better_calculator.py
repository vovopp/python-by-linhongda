num1 = float(input("請輸入第一個數字: "))
op = input("請輸入運算符號(+,-,*,/):")
num2 = float(input("請輸入第二個數字: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)   
else:
    print("沒有支援這種運算符號")