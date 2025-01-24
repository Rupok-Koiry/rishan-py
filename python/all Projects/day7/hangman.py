import random
logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''


print(f"HELLO SIR WELCOME TO THE {logo} GAME .")
end_of_game = False
lives = 7

word_list = ["apple",
             "lichi"
             ]

comp = random.choice(word_list)
# print(f"The solution is {comp}")
display = []
word_len = len(comp)
for _ in range(word_len):
    display += "_"

print(display)
while not end_of_game:
    guess = input("Enter a letter: ").lower()
    if guess in display:
        print(f"you have alredy guess {guess}")
    for position in range(word_len):
        letter = comp[position]
        if letter == guess:
            display[position] = letter
    if guess not in comp:
        print("You guess wrong")
        lives -= 1
        print(f"you lost a live you have {lives} lives")
        while lives == 0:
            end_of_game = True
            print("You lose")
            break
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win!")
    if lives == 6:
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========
''')
    elif lives == 5:
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========
# # ''')
    elif lives == 4:
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''')
    elif lives == 3:
        print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
    elif lives == 2:
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''')
    elif lives == 1:
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''')
    elif lives == 0:
        print(''' YOU ARE A KILLER
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

YOU LOST
''')

        break
word_list = ["apple", "mango", "banana", "grapes",
             "dragon", "tomato", "cucumber", "onion"]
v = random.choice(word_list)
a = len(v)
end_of_game = False
dis = []
print(f"guess a fruit name that has length of {a}")
for _ in range(len(v)):
    dis += "_"
while not end_of_game:
    user = input("Enter a letter:").lower()

for position in range(len(v)):

    letter = v[position]
    if letter == user:
        dis[position] = letter

    print(dis)
    if "_" not in dis:
        end_of_game = True
        print("you win")

world_list = ["advark", "babbon", "camel"]
com = random.choice(world_list)
display = []
end = False
for _ in range(len(com)):
    display += "_"
while not end:
    user = input("Enter a letter :").lower()
    for position in range(len(com)):
        letter = com[position]

        if letter == user:
            display[position] = letter

        print(display)
        if "_" not in display:
            end = True
            print("you win")
