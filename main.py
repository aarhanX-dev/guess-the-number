# THE PERFECT GUESS
import random
print("    <==WELCOME==>")
print("!---GUESS THE NUMBER---!")

n = random.randint(1, 100)
a = -1
att = 1
while(a!=n):
    a = int(input("enter guess (1-100): "))
    if(a>n):
        print("Lower number please!")
        att +=1
    elif(a<n):
        print("Higher number please!")
        att +=1
print(f"You won! You guessed it on your {att} attempt!")
print("<===END OF PROGRAM===>")
