# Написати гру "Бики і корови". Програма "загадує" чотиризначне число і 
# гравець має вгадати його. Після введення користувачем числа програма 
# повідомляє, скільки цифр числа вгадано (бики) і скільки цифр вгадано 
# і стоїть на потрібному місці (корови). Після відгадування числа на екран 
# необхідно вивести кількість спроб зроблених користувачем . 
# У програмі необхідно використовувати рекурсію.

import random

def count_bulls_and_cows(hidden_number, user_num):
    bulls = 0
    cows = 0
    
    for i in range(len(user_num)):
        if user_num[i] == hidden_number[i]:
            cows += 1
        elif user_num[i] in hidden_number: 
            bulls += 1
            
    return (bulls, cows)

def bulls_and_cows():
    hidden_number = str(random.randint(1000, 9999))
    user_num = ''
    
    while True:
        user_num = input("Enter four-digit number: ")
        
        if len(user_num) != 4 or not user_num.isdigit():
            print("Please enter a 4-digit number")
            continue
        
        bulls, cows = count_bulls_and_cows(hidden_number, user_num)
        
        print(f"{bulls} bulls | {cows} cows")
        
        if user_num == hidden_number:
            print("You win")
            break
        
        
        
        

bulls_and_cows()