"snake ,water ,game"
import random
'''
import random
comp = random.choice(["snake", "water", "gun"])
user = input("enter snake or water or gun :")


if comp == user:

    print("its a draw")

elif comp == "snake" and user == "gun":

    print("you win")


elif comp == "water" and user == "snake":

    print("comp  win")


elif comp == "gun" and user == "water":

    print("comp win")


elif comp == "gun" and user == "snake":

    print("comp win")


elif comp == "water" and user == "gun":

    print("comp win")


elif comp == "snake" and user == "water":

    print("you win")
else:
    print("something went wrong")


print(f"computer was  chose : {comp}")


print(f"you  was  chose : {user}")
'''


"rock,paper,siscor"
'''



import random
name = input("enter your name:")


print(f"hi {name} pls try my first game!")


enter = input("")


def game(comp, you):

    if comp == you:
        return None
    elif (comp == 'r' and you == 'p') or (comp == 'p' and you == 's') or (comp == 's' and you == 'r'):
        return True
    else:
        return False


run = random.randint(1, 3)
if run == 1:
    comp = "r"
elif run == 2:
    comp = "p"
elif run == 3:
    comp = "s"


b = input("Your turn: rock (r), paper (p), or scissors (s): ").lower()


if b not in ['r', 'p', 's']:
    print("invalid input!!!!!!!!! Please enter 'r' for rock, 'p' for paper, or 's' for scissors.")
else:
    you = b

    result = game(comp, you)

    print(f"Computer chose: {comp}")
    print(f"You chose: {you}")

    if result is None:
        print("This game is a tie.")
    elif result:
        print(f"{name} win!")
    else:
        print(f"{name} lose!")

'''
"calculator"

'''
num1 = float(input("\"enter your first number\":"))

num3 = float(input("\"enter your third  number\":"))
bb = input(" enter what do you want to\" +,- ,*,%\":  ")
if bb == "+":
    print(num1 + num3)
elif bb == "-":
    print(num1 - num3)
elif bb == "*":
    print(num1 * num3)
else:
    print(num1 % num3)

'''

"guessnumber"
'''

from random import randint
n = int(input("\"how much time you want to play this game:\""))
for x in range(n):
    guessnumber = int(input("\"enter your guess betwwen 1 to 10 :\""))
    randomnumber = randint(1, 10)
    if guessnumber == randomnumber:
        print("you won")
        print("\"THE GAME DESIGNED BY RISHAN KOIRY\"")
    else:
        print("you have lost")
        print("\"computer number was :\"", randomnumber)
        print("\"THE GAME DESIGNED BY RISHAN KOIRY\"")
'''
"time program"
'''
import datetime
print(
    "you can get in this program month ,year,sechond,hour,weekend,minute,end")
a = datetime.datetime.now()
bro = (input("enter what you want :"))
if bro == "month":
    print(a.strftime("%m"))
elif bro == "year":
    print(a.strftime("%Y"))
elif bro == "date":
    print(a.strftime("%D"))
elif bro == "hour":
    print(a.strftime("%H"))
elif bro == "sechond":
    print(a.strftime("%S"))
elif bro == "minute":
    print(a.strftime("%M"))
else:
    print("why are you where thats a time program")

'''

"math"
'''
width = float(input("enter your width:"))
height = float(input("enter your height:"))
oparetion = (
    input("enter what do you want to do : triangle, :square ,:circle:"))
if oparetion == "triangle":
    print(0.5*width * height)
    print("the program    made by--RISHAN-KOIRY")
elif oparetion == "square":
    print(width*height)
    print("the program  made by---RISHAN-KOIRY")
elif oparetion == "circle":
    print(3.1416*width*height)
    print(" the program  made  by---RISHAN-KOIRY")
else:
    print("\"this program is for  triangle, square ,circle  (area) made by (\" RISHAN - KOIRY\")\"")
'''
"table"
'''
n = int(input("Enter your number: "))
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")
'''

"vowel and consonent"
'''
bb = input(" your alphabet  \t")
if bb == "a" or bb == "e" or bb == "i" or bb == "o" or bb == "u":
    print("volwel")
else:
    print("consonent")
'''
"number game"


'''a = int(input("enter your number:"))
n = random.randint(1, 100)
b = -1
guess = 0
while b != n:
    guess += 1
    if a > n:
        print("lower number please")
    elif a < n:
        print("higher number please")
    else:
        print("higher number please")
print(f"you have gueesd the number{n}correctly{guess}attpemnts")'''


'''
print("WELCOME TO THE TIP CALCULATOR.")
n = input("ENTER YOUR CURRENCY NAME:")
a = int(input("WHAT IS THE TOTAL BILL? :"))
b = int(input("HOW MANY PEOPLE TO SPILT THE BILL? :"))
c = int(input("what percentage tip do you like to give :"))

money = a/b
x = money*c


if c == 0:
    print("EACH PERSON SHOULD PAY ", money, n)
else:
    print("EACH PERSON SHOULD PAY", x, n)
    '''


'''love calculator'''

'''name = input("enter your name:")
name1 = input("enter her name:")
n = name+name1
lower = n.lower()

t = lower.count("t")
r = lower.count("r")
u = lower.count("u")
e = lower.count("e")
true = t+r+u+e
l = lower.count("l")
o = lower.count("o")
user = lower.count("user")
e = lower.count("e")
love = l+o+user+e
x = str(true)+str(love)
user = int(x)


if user > 20:
    print(f"{name} love is good to {name1}")
elif user > 50:
    print(f"{name} you are best with {name1}")
else:
    print("100% love love love o 100% love love love ")'''


'''pizza maneger'''

'''print("Hey sir, welcome to Pizza Rishan!")

# Get the size of the pizza
size = input(
    "Which size pizza do you want? Enter 's' for small, 'm' for medium, 'l' for large: ")

# Get the preference for onions
onion = input(
    "Do you want onions in your pizza? Enter 's' for some, 'm' for medium, 'user' for very much: ")

# Get the preference for extra cheese
cheese = input(
    "Do you want extra cheese on your pizza? Enter 'y' for yes, 'n' for no: ")

# Initialize the bill
bill = 0

# Calculate the cost based on pizza size
if size == 's':
    bill += 100
    size_name = "small"
elif size == 'm':
    bill += 300
    size_name = "medium"
elif size == 'l':
    bill += 500
    size_name = "large"
else:
    print("Invalid size selected!")
    size_name = None

# If a valid size was selected, proceed with additional options
if size_name:
    # Calculate the cost based on onion preference
    if onion == 's':
        bill += 10
        onion_amount = "some"
    elif onion == 'm':
        bill += 20
        onion_amount = "medium"
    elif onion == 'user':
        bill += 30
        onion_amount = "very much"
    else:
        print("Invalid onion amount selected!")
        onion_amount = None

    # Calculate the cost based on extra cheese preference
    if cheese == 'y':
        bill += 40
        cheese_extra = "with extra cheese"
    elif cheese == 'n':
        cheese_extra = "without extra cheese"
    else:
        print("Invalid cheese option selected!")
        cheese_extra = None

    # Print the final bill if all options were valid
    if onion_amount and cheese_extra:
        print(f"You ordered a {size_name} pizza {
              cheese_extra} and {onion_amount} onions.")
        print(f"Your total bill is {bill} tk.")

# Output in case of invalid options
if not size_name or not onion_amount or not cheese_extra:
    print("There was an error with your order. Please try again.")
import random
size = input("ENTER YOUR PIZZA SIZE  SMALL OR MEDIUM OR LARGE:")
onion = input("DO YOU WANT ONION IN PIZZA :")
chess = input("DO YOU NEED CHESS IN PIZZA :")
bill = 0
if size == "small":
    print("small size pizza is 100 tk")
    bill = bill+100
elif size == "medium":
    print("medium size pizza is 250tk")
    bill = bill+250
elif size == "large":
    print("large size pizza is 500tk")
    bill = bill+500
if onion == "some":
    print("your onion price 5tk")
    bill = bill+5
elif onion == "medium":
    print("your onion price 15tk")
    bill = bill+15
elif onion == "so much":
    print("your onion price 50tk")
    bill = bill+50
if chess == "some":
    print("your chess price 10tk")
    bill = bill+10
elif chess == "medium":
    print("your chess price 20tk")
    bill = bill+20
elif chess == "so much":
    print("your chess price 50tk")
    bill = bill+50
user = input("SIR IS THAT YOUR ORDER.")
print(f"SIR YOUR BILL IS {bill}")
bill = 0

a = int(input("ENTER YOUR HEIGHT IN CM:"))
if a > 120:
    print("you can ride rolar closter")
    b = int(input("enter your age:"))
    if b <= 5:
        print("your need  5$")
        bill += 5
    elif b >= 6:
        print("your need  10$")
        bill += 10
    elif b > 20:
        print("you need 20$")
        bill += 20
    p = input("do you want a photo:")
    if p == "yes":
        print("you need 3 $")
        bill += 3
    elif p == "no":
        print("ok")
    print(f" thanks, your total bill is {bill}$")'''


'''trusure game'''


# road = random.choice(["left", "right"])
# xv = random.choice(["swim", "wait"])
# door = random.choice(["red", "yellow", "blue"])
# noob = input("you think you are a noob if think enter noob :")
# if noob == "noob":
#     print(f"if your choice and computer choice=you win or you lost you say you are a noob so i  give you the computer move\n{
#           road} is the first move {xv} is the sechond move and third move is {door} if you enter this move you will win.")
# else:
#     print("ok play the game you will understand")
# print("Think you are the middle of island")
# roaduser = input("Enter left or right :")

# if roaduser == road:
#     print("now you are in small boat")
#     xvuser = input("Enter do you want to swim or wait for a boat  :")
#     if xvuser == xv:
#         print("you in a village")
#         dooruser = input("Chose a door red,blue,yellow  :")
#         if dooruser == door:
#             print("you won")
#             print(''' you got a trusere chest !!!!!!!!!!!


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
#         elif door != dooruser:
#             print("you lost")
#     elif xvuser != xv:
#         print("you lost pirana eats you")

# elif roaduser != road:
#     print("you lost monster eat you")


'''higher_lower'''


'''import random
logo = """
    __  ___       __
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /
/_/ ///_/\__, /_/ /_/\___/_/
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /
/_____/\____/|__/|__/\___/_/
"""


vs = """
 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)
"""

print(logo)
should_continue = True
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and Model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 90,
        'description': 'Reality TV personality',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country': 'United States'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 87,
        'description': 'Comedian',
        'country': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 86,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 85,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Rihanna',
        'follower_count': 81,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': "Victoria's Secret",
        'follower_count': 69,
        'description': 'Lingerie brand',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 68,
        'description': 'Actress and musician',
        'country': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 66,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Drake',
        'follower_count': 65,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 67,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 82,
        'description': 'Footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 59,
        'description': 'Musician and actor',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 56,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 57,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 54,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 53,
        'description': 'Actress and musician',
        'country': 'India'
    },
    {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country': 'China'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]


score = 0
should_continue = True

while should_continue:
    comp = random.choice(data)
    comp_2 = random.choice(data)

    while comp == comp_2:
        comp_2 = random.choice(data)

    print("a =>")
    print(f"name: {comp["name"]}")
    print(f"work: {comp["description"]}")
    print(f"location: {comp["country"]}")

    print(vs)

    print(f"b =>")
    print(f"name: {comp_2["name"]}")
    print(f"work: {comp_2["description"]}")
    print(f"location: {comp_2["country"]}")

    user_choice = input(
        "who has more followers (a) for the first, (b) for the second: ")

    if user_choice == "a" and comp["follower_count"] > comp_2["follower_count"]:
        score += 1
        print(f"You are correct! {comp['name']} has {
              comp['follower_count']} million followers.")
    elif user_choice == "b" and comp_2["follower_count"] > comp["follower_count"]:
        score += 1
        print(f"You are correct! {comp_2['name']} has {
              comp_2['follower_count']} million followers.")
    else:
        print(f"You are wrong! {comp['name']} has {comp['follower_count']} million followers, "
              f"and {comp_2['follower_count']} million followers.")
        should_continue = False


print(f"Your score is: {score}")
'''


'''hangman'''

# logo = '''
#  _
# | |
# | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
# | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
# | | | | (_| | | | | (_| | | | | | | (_| | | | |
# |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                     __/ |
#                    |___/    '''


# print(f"HELLO SIR WELCOME TO THE {logo} GAME .")
# end_of_game = False
# lives = 7

# word_list = ['abruptly',
#              'absurd',
#              'abyss',
#              'affix',
#              'askew',
#              'avenue',
#              'awkward',
#              'axiom',
#              'azure',
#              'bagpipes',
#              'bandwagon',
#              'banjo',
#              'bayou',
#              'beekeeper',
#              'bikini',
#              'blitz',
#              'blizzard',
#              'boggle',
#              'bookworm',
#              'boxcar',
#              'boxful',
#              'buckaroo',
#              'buffalo',
#              'buffoon',
#              'buxom',
#              'buzzard',
#              'buzzing',
#              'buzzwords',
#              'caliph',
#              'cobweb',
#              'cockiness',
#              'croquet',
#              'crypt',
#              'curacao',
#              'cycle',
#              'daiquiri',
#              'dirndl',
#              'disavow',
#              'dizzying',
#              'duplex',
#              'dwarves',
#              'embezzle',
#              'equip',
#              'espionage',
#              'mango',
#              'exodus',
#              'faking',
#              'fishhook',
#              'fixable',
#              'fjord',
#              'flapjack',
#              'flopping',
#              'fluffiness',
#              'flyby',
#              'foxglove',
#              'frazzled',
#              'frizzled',
#              'fuchsia',
#              'funny',
#              'gabby',
#              'galaxy',
#              'galvanize',
#              'gazebo',
#              'giaour',
#              'gizmo',
#              'glowworm',
#              'glyph',
#              'gnarly',
#              'gnostic',
#              'gossip',
#              'grogginess',
#              'haiku',
#              'haphazard',
#              'hyphen',
#              'iatrogenic',
#              'icebox',
#              'injury',
#              'ivory',
#              'ivy',
#              'jackpot',
#              'jaundice',
#              'jawbreaker',
#              'jaywalk',
#              'jazziest',
#              'jazzy',
#              'jelly',
#              'jigsaw',
#              'jinx',
#              'jiujitsu',
#              'jockey',
#              'jogging',
#              'joking',
#              'jovial',
#              'joyful',
#              'juicy',
#              'jukebox',
#              'jumbo',
#              'kayak',
#              'kazoo',
#              'keyhole',
#              'khaki',
#              'kilobyte',
#              'kiosk',
#              'kitsch',
#              'kiwifruit',
#              'klutz',
#              'knapsack',
#              'larynx',
#              'lengths',
#              'lucky',
#              'luxury',
#              'lymph',
#              'marquis',
#              'matrix',
#              'megahertz',
#              'microwave',
#              'mnemonic',
#              'mystify',
#              'naphtha',
#              'nightclub',
#              'nowadays',
#              'numbskull',
#              'nymph',
#              'onyx',
#              'ovary',
#              'oxidize',
#              'oxygen',
#              'pajama',
#              'peekaboo',
#              'phlegm',
#              'pixel',
#              'pizazz',
#              'pneumonia',
#              'polka',
#              'pshaw',
#              'psyche',
#              'puppy',
#              'puzzling',
#              'quartz',
#              'queue',
#              'quips',
#              'quixotic',
#              'quiz',
#              'quizzes',
#              'quorum',
#              'razzmatazz',
#              'rhubarb',
#              'rhythm',
#              'rickshaw',
#              'schnapps',
#              'scratch',
#              'shiv',
#              'snazzy',
#              'sphinx',
#              'spritz',
#              'squawk',
#              'staff',
#              'strength',
#              'strengths',
#              'stretch',
#              'stronghold',
#              'stymied',
#              'subway',
#              'swivel',
#              'syndrome',
#              'thriftless',
#              'thumbscrew',
#              'topaz',
#              'transcript',
#              'transgress',
#              'transplant',
#              'triphthong',
#              'twelfth',
#              'twelfths',
#              'unknown',
#              'unworthy',
#              'unzip',
#              'uptown',
#              'vaporize',
#              'vixen',
#              'vodka',
#              'voodoo',
#              'vortex',
#              'voyeurism',
#              'walkway',
#              'waltz',
#              'wave',
#              'wavy',
#              'waxy',
#              'wellspring',
#              'wheezy',
#              'whiskey',
#              'whizzing',
#              'whomever',
#              'wimpy',
#              'witchcraft',
#              'wizard',
#              'woozy',
#              'wristwatch',
#              'wyvern',
#              'xylophone',
#              'yachtsman',
#              'yippee',
#              'yoked',
#              'youthful',
#              'yummy',
#              'zephyr',
#              'zigzag',
#              'zigzagging',
#              'zilch',
#              'zipper',
#              'zodiac',
#              'zombie',
#              ]

# comp = random.choice(word_list)

# display = []
# word_len = len(comp)
# for _ in range(word_len):
#     display += "_"

# print(display)
# while not end_of_game:
#     guess = input("Enter a letter: ").lower()
#     if guess in display:
#         print(f"you have alredy guess {guess}")
#     for position in range(word_len):
#         letter = comp[position]
#         if letter == guess:
#             display[position] = letter
#     if guess not in comp:
#         print("You guess wrong")
#         lives -= 1
#         print(f"you lost a live you have {lives} lives")
#         while lives == 0:
#             end_of_game = True
#             print("You lose")
#             break
#     print(display)
#     if "_" not in display:
#         end_of_game = True
#         print("You win!")
#     if lives == 6:
#         print('''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''')
#     elif lives == 5:
#         print('''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# # # ''')
#     elif lives == 4:
#         print('''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''')
#     elif lives == 3:
#         print('''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''')
#     elif lives == 2:
#         print('''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''')
#     elif lives == 1:
#         print('''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''')
#     elif lives == 0:
#         print(''' YOU ARE A KILLER
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========

# YOU LOST
# ''')

#         break
# word_list = ["apple", "mango", "banana", "grapes",
#              "dragon", "tomato", "cucumber", "onion"]
# user = random.choice(word_list)
# a = len(user)
# end_of_game = False
# dis = []
# print(f"guess a fruit name that has length of {a}")
# for _ in range(len(user)):
#     dis += "_"
# while not end_of_game:
#     user = input("Enter a letter:").lower()

# for position in range(len(user)):

#     letter = user[position]
#     if letter == user:
#         dis[position] = letter

#     print(dis)
#     if "_" not in dis:
#         end_of_game = True
#         print("you win")

# world_list = ["advark", "babbon", "camel"]
# com = random.choice(world_list)
# display = []
# end = False
# for _ in range(len(com)):
#     display += "_"
# while not end:
#     user = input("Enter a letter :").lower()
#     for position in range(len(com)):
#         letter = com[position]

#         if letter == user:
#             display[position] = letter

#         print(display)
#         if "_" not in display:
#             end = True
#             print("you win")
'''Quiz game'''


"quiz game"
# question_data = [
#     {"text": "Honey never spoils.", "answer": "True"},
#     {"text": "The average person will shed 10 pounds of skin in their lifetime.",
#         "answer": "False"},
#     {"text": "Bananas are berries, but strawberries are not.", "answer": "True"},
#     {"text": "Humans share 50% of their DNA with bananas.", "answer": "True"},
#     {"text": "The Eiffel Tower can be 15 cm taller during the summer.", "answer": "True"},
#     {"text": "An octopus has three hearts.", "answer": "True"},
#     {"text": "The shortest war in history lasted 38 minutes.", "answer": "True"},
#     {"text": "A group of flamingos is called a 'flamboyance'.", "answer": "True"},
#     {"text": "A crocodile can't stick its tongue out.", "answer": "True"},
#     {"text": "The unicorn is the national animal of Scotland.", "answer": "True"},
#     {"text": "Coca-Cola was originally green.", "answer": "False"},
#     {"text": "Polar bear fur is white.", "answer": "False"},
#     {"text": "Goldfish only have a memory span of three seconds.", "answer": "False"},
#     {"text": "Sloths can hold their breath longer than dolphins.", "answer": "True"},
#     {"text": "The Great Wall of China is visible from space.", "answer": "False"},
#     {"text": "Bats are blind.", "answer": "False"},
#     {"text": "The Empire State Building can fit inside the Eiffel Tower.", "answer": "False"},
#     {"text": "The shortest commercial flight in the world lasts just 57 seconds.", "answer": "True"},
#     {"text": "A sneeze travels at about 100 miles per hour.", "answer": "True"},
#     {"text": "Elephants are the only animals that can't jump.", "answer": "True"},
#     {"text": "Venus is the hottest planet in the solar system.", "answer": "True"},
#     {"text": "Mount Everest is the closest point on Earth to space.", "answer": "False"},
#     {"text": "A group of owls is called a 'parliament'.", "answer": "True"},
#     {"text": "Sharks are mammals.", "answer": "False"},
#     {"text": "Humans have more taste buds than cats.", "answer": "True"},
#     {"text": "There are more stars in the universe than grains of sand on all Earth's beaches.", "answer": "True"},
#     {"text": "A cat has 32 muscles in each ear.", "answer": "True"},
#     {"text": "A jiffy is an actual unit of time.", "answer": "True"},
#     {"text": "The smallest bone in the human body is the stirrup bone in the ear.", "answer": "True"},
#     {"text": "A shrimp's heart is located in its head.", "answer": "True"},
#     {"text": "Humans share 99% of their DNA with chimpanzees.", "answer": "True"},
#     {"text": "Lightning never strikes the same place twice.", "answer": "False"},
#     {"text": "A single strand of spaghetti is called a 'spaghetto'.", "answer": "True"},
#     {"text": "The Sahara Desert is the largest desert on Earth.", "answer": "False"},
#     {"text": "A day on Venus is longer than a year on Venus.", "answer": "True"},
#     {"text": "Penguins can fly.", "answer": "False"},
#     {"text": "The moon is moving away from Earth at a rate of about 1.6 inches per year.", "answer": "True"},
#     {"text": "Humans can distinguish over a trillion different smells.", "answer": "True"},
#     {"text": "A jellyfish is 95% water.", "answer": "True"},
#     {"text": "The human nose can detect 1 trillion different scents.", "answer": "True"},
#     {"text": "Some turtles can breathe through their butts.", "answer": "True"},
#     {"text": "An ostrich's eye is bigger than its brain.", "answer": "True"},
#     {"text": "The Amazon Rainforest produces 20% of Earth's oxygen.", "answer": "False"},
#     {"text": "You can see the Great Wall of China from the moon.", "answer": "False"},
#     {"text": "The human brain is the most energy-consuming organ in the body.",
#         "answer": "True"},
#     {"text": "Octopuses have blue blood.", "answer": "True"},
#     {"text": "There are more fake flamingos in the world than real ones.", "answer": "True"},
#     {"text": "Humans have 4 different blood types.", "answer": "True"}
# ]

# should_continue = True
# score = 0
# question = 0
# right_ans = 0
# while should_continue:

#     comp = random.choice(question_data)
#     question += 1
#     user = input(f"{question}) Question: {
#                  comp["text"]} :  Enter True or False : ")
#     print()

#     answer_checker = comp["answer"]

#     if user == "False" and answer_checker == "True":
#         print("You lost That Was True😵.")
#         print(f"You Answer {
#               question} question and you got right {right_ans} .")
#         should_continue = False

#     elif user == "True" and answer_checker == "False":
#         print("You lost That Was False😵.")
#         print(f"You Answer {
#               question} question and you got right {right_ans} .")
#         should_continue = False

#     elif user == answer_checker:
#         right_ans += 1
#         print("Congratulations, You Win 😊.")
#         print()
#         print(f"You Answer {
#               question} question and you got right {right_ans} .")
#         print()
