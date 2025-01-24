# student_heights = input('Student Heights: ').split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total = 0
# num = 0
# for height in student_heights:
#     total += height
#     num += 1
# print(f"Average {total/num}")

# total = 0
# for num in range(2, 102, 2):
#     total += num
# print(total)

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print("Buzz")

#     else:
#         print(num)


# Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = []

# for i in range(1, nr_letters+1):
#     password.append(random.choice(letters))
# for i in range(1, nr_symbols+1):
#     password.append(random.choice(symbols))

# for i in range(1, nr_numbers+1):
#     password.append(random.choice(numbers))
# random.shuffle(password)
# print("".join(password))
