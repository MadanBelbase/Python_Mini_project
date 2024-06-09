import random
your_win = 0
pc_win = 0
options = ["rock","paper","scissors"]
 
while True:
    input1 = input("Enter the number\nRock\paper\scissors\Q for quit game\n").lower()
    if input1 =="q":
        break

    if input1 not in options:
        print("Please select vaild key/option")
        continue
        
    
    number = random.randint(0,2)
    pc_choose = options[number]

    print(f" computer choose number is: {pc_choose}")
    if input1 == "rock" and pc_choose == "scissors":
        print("you win!")
        your_win = your_win + 1
        continue
       
    elif input1 == "paper" and pc_choose == "rock":
        print("You won!")
        your_win = your_win+1
        continue

       
    elif input1 == "scissors" and  pc_choose == "paper":
        print("You won!")
        your_win = your_win + 1
        continue
    
    elif input1 == pc_choose:
        print("draw")
        
    else:
        print("You lose")
        pc_win = pc_win+1
print(f"you win {your_win} times")
print(f"computer win {pc_win} times")
print("Have a good day ")




      