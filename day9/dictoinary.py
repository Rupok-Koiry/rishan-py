# student_scores = {
#     "harry": 81,
#     "ron": 78,
#     "heromine": 99,
#     "draco": 74,
#     "nevelie": 62
# }
# student_grades = {}
# for i in student_scores:
#     scores = student_scores[i]

#     if scores > 90:
#         student_grades[i] = "outstanding"
#     elif scores < 90:
#         student_grades[i] = "good"
#     elif scores < 70:
#         student_grades[i] = "fail"
# print(student_grades)
# import random
# wordlist = ["apple", "mango", "civel"]
# com = random.choice(wordlist)
# game = True
# display = []
# print(com)
# for _ in range(len(com)):
#     display += "_"
# print(display)
# while game:
#     user = input("enter a letter:")
#     for position in range(len(com)):
#         letter = com[position]

#         if letter == user:
#             display[position] = letter
#             print(display)
#         if "_" not in display:

#             print("you win")
#             game = True
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


# def add_new_country(country, visit, cities):
#     adedd = travel_log.append({
#         "country": country,
#         "visits": visit,
#         "cities": cities

#     }
#     )

#     print(travel_log)


# add_new_country(country="bangladesh", visit=1, cities=["dhaka", "khulna"])


# 🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
# def new():
#     country = {}
'bid program'
# print("Welcome to the bid program.")
# game = True


# def high(beding_record):
#     highest = 0
#     for bidder in beding_record:
#         bid_amounth = beding_record[bidder]
#         if bid_amounth > highest:
#             highest = bid_amounth
#             winner = bidder
#             print(f"the winner is {winner} with a bid of ${highest}")


# def bids(name, money):
#     bid = {"names": name,
#            "moneys": money

#            }
#     print(bid)


# while game:
#     user_name = input("Enter your name :")
#     user_money = int(input("Enter you bid :"))

#     bids(user_name, user_money)
#     another_user = input("is there another bider :")
#     if another_user == "yes":
#         game = True
#         print("\033c")

#     else:
#         game = False
#         high(bids)
# print("Welcome to the bid program.")
# game_active = True
# bidding_records = {}


# def get_highest_bid(bidding_records):
#     highest_bid = 0
#     winner = ""
#     for bidder, bid_amount in bidding_records:
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")


# def add_bid(name, amount):
#     bidding_records[name] = amount


# while game_active:
#     user_name = input("Enter your name: ")
#     user_bid = int(input("Enter your bid: "))

#     add_bid(user_name, user_bid)

#     another_user = input("Is there another bidder? (yes/no): ").lower()
#     if another_user == "yes":
#         print("\033c")
#     else:
#         game_active = False
#         get_highest_bid(bidding_records)
# lists = [10, 20, 30, 76268, 8398, 923766]
# higsoc = 0
# for i in lists:
#     if i > higsoc:
#         higsoc = i
# print(f"highscon is {higsoc}")
# number = int(input("enter :"))
# is_prime = True

# for i in range(2, number):
#     if number % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print("The number is a prime number")
# else:
#     print("The number is not a prime number")
# for num in range(1, 101):
#     if num > 1:  # Prime numbers are greater than 1
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num)
