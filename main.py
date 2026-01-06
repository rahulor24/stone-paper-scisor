'''
1 for stone (a)
-1 for paper (s)
0 for scisor (d)
'''

import random

computer=random.choice([-1,0,1])

dict={"a":1, "s":-1, "d":0}
choice={1:"stone", -1:"paper", 0:"scisor"}

choose=input("""type 'a' for stone
type 's' for paper
type 'd' for scisor
""")

you=dict[choose]

print(f"You chose {choice[you]}\nComputer chose {choice[computer]}")

if computer==you:
    print("It's a draw")
else:
    if computer==1 and you==-1:
        print("You win!")
    elif computer==1 and you==0:
        print("You lose!")
    elif computer==-1 and you==1:
        print("You lose!")
    elif computer==-1 and you==0:
        print("You win!")
    elif computer==0 and you==1:
        print("You win!")
    elif computer==0 and you==-1:
        print("You lose!")
    else:
        print("Something went wrong!!")