from asyncio import base_tasks
import random

user_wins = 0
computer_wins = 0
options = ["石頭","布","剪刀"]

while True: 
    user_input = input("石頭/布/剪刀 or Q to quit: ").lower()
    if user_input == "q":
        break 
        
    if user_input not in options: 
        continue 
        
    random_number = random.randint(0,2)
    #石頭:0,布:1,剪刀:2
    computer_pick = options[random_number]
    print("對方選擇", computer_pick + ".")

    if user_input == "石頭" and computer_pick == "剪刀":
        print("恭喜你贏了")
        user_wins += 1

    elif user_input == "布" and computer_pick == "石頭":
        print("恭喜你贏了")
        user_wins += 1
    
    elif user_input == "剪刀" and computer_pick == "布":
        print("恭喜你贏了")
        user_wins += 1
    
    elif user_input == computer_pick:
        print("平手")
    else:
        print("可惜 你輸了")
        computer_wins += 1

print("你贏了",user_wins,"次")
print("對方贏了",computer_wins,"次")

print("下次再來") 