import random
def cheque(AI,user):
    if(AI == user):
        return 0
    if(AI==0 and user==1):
        return -1
    if(AI==1  and user==2):
         return -1
    if(AI == 2 and user==0):
        return -1
    return 1
AI = random.randint(0,2)
user = int(input("0 for snake , 1 for water and 2 for gun :\n"))
score = cheque(AI , user)
print("You:",user)
print("AI:",AI)
if(score==0):
    print("Draw the game")
elif(score == -1):
    print("You lose")
else:
    print("You won")
