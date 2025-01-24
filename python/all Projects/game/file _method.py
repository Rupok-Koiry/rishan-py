import os

# 1. Opening a File
file = open('example.txt', 'r')  # Open for reading (default)
file.close()  # Always good practice to close the file when done

# 2. Reading a File
with open('example.txt', 'r') as file:
    content = file.read()
    print('Read content:')
    print(content)

# 3. Writing to a File
with open('example.txt', 'w') as file:
    file.write('Hello, world!')
    print('Written "Hello, world!" to example.txt')

# 4. Appending to a File
with open('example.txt', 'a') as file:
    file.write('Appending this line.\n')
    print('Appended "Appending this line." to example.txt')

# 5. Reading Line by Line
print('Reading file line by line:')
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

# 6. Reading All Lines
print('\nReading all lines into a list:')
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

# 7. Closing a File
file = open('example.txt', 'r')
content = file.read()
file.close()
print('\nRead content using close:')
print(content)

# 8. Checking if a File Exists
if os.path.exists('example.txt'):
    print('File exists.')
else:
    print('File does not exist.')

# 9. Removing a File
if os.path.exists('example.txt'):
    os.remove('example.txt')
    print('File removed.')
else:
    print('File does not exist.')

# Recreate the file for the next step
with open('example.txt', 'w') as file:
    file.write('Hello, world!')

# 10. Renaming a File
if os.path.exists('example.txt'):
    os.rename('example.txt', 'new_example.txt')
    print('File renamed to new_example.txt.')
else:
    print('File does not exist.')

# Clean up: remove the new_example.txt file
if os.path.exists('new_example.txt'):
    os.remove('new_example.txt')
    print('Cleanup: new_example.txt removed.')
