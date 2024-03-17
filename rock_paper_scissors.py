#rock(1) paper scissors(3)#
#rock(1) win against scissors(3)#
#scissors(3) win agansit paper(2)#
#paper(1) win aganist rock(2)#
import random
user=int(input("enter the choice:\n 0 for rock\n 1 for paper\n 2 for scissors\n"))
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper ="""
  _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissiors="""
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
list =[rock,paper,scissiors]
if user>=3 or user<0:
    print("inavalid values:\n'enter the choice:\n 0 for rock\n 1 for paper\n 2 for scissors\n'")
else:
    computer_choice = random.randint(0, 2)
    if user == computer_choice:
        print("it a draw")
    elif computer_choice == user:
        print("it a draw")
    elif user == 2 and computer_choice == 1:
        print("your win",list[user],list[computer_choice])
    elif computer_choice == 2 and user == 0:
        print("you loss",list[user],list[computer_choice])
    elif user > computer_choice:
        print("you win",list[user],list[computer_choice])
    elif computer_choice > user:
        print("you loss",list[user],list[computer_choice])






