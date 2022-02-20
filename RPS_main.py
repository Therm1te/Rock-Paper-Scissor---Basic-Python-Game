#Rock, Paper, Scissor Game made through the help of Harry bhai and a little bit of my innovation
import random

def PlayerGameWin(C1, P1):
    if C1 == P1:
        return None

    elif C1 == 'R':
        if P1 == "P":
            return True
        elif P1 == "S":
            return False

    elif C1 == 'P':
        if P1 == "R":
            return False
        elif P1 == "S":
            return True
            
    elif C1 == 'S':
        if P1 == "R":
            return True
        elif P1 == "P":
            return False 


randNo = random.randint(1, 3) 
if randNo == 1:
    C1 = 'R'
elif randNo == 2:
    C1 = 'P'
elif randNo == 3:
    C1 = 'S'


P1 = input("Player 1, Rock(R), Paper(P) or Scissor(S)?")
A = PlayerGameWin(C1, P1)            

print(f"Computer chose {C1}")
print(f"Player chose {P1}")

if C1 == 'R':
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

elif C1 == 'P':
    print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''')

elif C1 == 'S':
    print('''
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

# Player 1 Emojis

if P1 == 'R':
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

elif P1 == 'P':
    print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''')

elif P1 == 'S':
    print('''
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

if A == None:
    print("Game Tied")
elif A:
    print("Player 1 Wins")
else:
    print("Player 1 Loses")

