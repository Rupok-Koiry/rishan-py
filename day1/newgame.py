import random
road = random.choice(["left", "right"])
xv = random.choice(["swim", "wait"])
door = random.choice(["red", "yellow", "blue"])
noob = input("you think you are a noob if think enter noob :")
if noob == "noob":
    print(f"if your choice and computer choice=you win or you lost you say you are a noob so i  give you the computer move\n{
          road} is the first move {xv} is the sechond move and third move is {door} if you enter this move you will win.")
else:
    print("ok play the game you will understand")
print("Think you are the middle of island")
roaduser = input("Enter left or right :")

if roaduser == road:
    print("now you are in small boat")
    xvuser = input("Enter do you want to swim or wait for a boat  :")
    if xvuser == xv:
        print("you in a village")
        dooruser = input("Chose a door red,blue,yellow  :")
        if dooruser == door:
            print("you won")
            print(''' you got a trusere chest !!!!!!!!!!!


                  _________________________
#        /#########################\\
#       /############################\\
#      /##############################\\
#     |####### ______   ______  #######|
#     |###### /      \\ /      \\ #######|
#     |######|  $$$$$$|$$$$$$  |#######|
#     |######| $$ | $$|$$ | $$ |#######|
#     |######| $$ | $$|$$ | $$ |#######|
#     |######| $$__/ $$| $$__/  |#######|
#     |###### \\$$    $$| $$     |#######|
#     |####### \\$$$$$$ | $$$$$$ |#######|
#     |########################### ######|
#     |########################### ######|
#     |### /-------------------------\\ ###|
# #     \\##/                           \\##/
# #       /                             \\
# #      /_______________________________\\''')
        elif door != dooruser:
            print("you lost")
    elif xvuser != xv:
        print("you lost pirana eats you")

elif roaduser != road:
    print("you lost monster eat you")
