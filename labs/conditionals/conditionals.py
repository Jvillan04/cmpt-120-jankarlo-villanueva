'''
Assignment #5:

    Tests the various capabilities of the functions  
    defined in the conditionals.py file.


@author Kevin Hayden
@date 2023-02-11
@org Marist College - Department of Computing Science

Syntax for single decision:

if <condition> :
    <body>
    
Syntax for 2-way decision:

if <condition> :
    <body>
else:
    <body>

Syntax for Multi-way decision:

if <condition> :
    <body>
elif <condition> :
    <body>
else:
    <body>
    
Syntax for try/catch:

try:
    <body>
except <exception-type> :
    <body>
'''

#Function to check for equilateral
def is_equilateral(x, y, z):
    if type(x) != int:
        raise Exception("x has to be an integer!")
    if type(y) != int:
        raise Exception("y has to be an integer!")
    if type(x) != int:
        raise Exception("x has to be an integer!")
    if type(z) != int:
        raise Exception("z has to be an integer!")
    if x == y == z:
        return True
    else:
        return False
    

#Function to check for vowels
def get_vowels(text):
    if type(text) != str:
        raise Exception("Only enter a string!")
    vowels = []
    for char in text:
        if char.lower() == ("a"):
            vowels.append(char)
        elif char.lower() == ("e"):
            vowels.append(char)
        elif char.lower() == ("i"):
            vowels.append(char)
        elif char.lower() == ("o"):
            vowels.append(char)
        elif char.lower() == ("u"):
            vowels.append(char)
    return vowels

#Function to validate list

def validate_list(grades):
    if type(grades) != list:
        raise Exception("You must enter a list!")
    elif grades == []:
        raise Exception("The list cannot be empty!")
    for n in grades:
        if type(n) != int:
            raise Exception("List must be only integers!")
        elif 0 > n or n > 100:
            raise Exception("Integers must be between 0 and 100!")
    else:
        return grades


#This is a function to check for palindrome
#[::1] reverses the string using slicing
#text.lower() allows for the function to handle capital letters

def is_palindrome(text):
  if type(text) != str:
    raise Exception("You must enter a string!")
  x = text.lower()
  if x == x[::-1]:
    return True
  else:
    return False

#Function to calculate grade average and letter
#Average is the sum divided by amount amount of numbers there are
#sum(grades) takes the sum of the list and len(grades) divides the sum by the amount of items in the list to get the average
def calculate_letter_grade(grades):
  average = sum(grades) / len(grades)
  if average >= 93:
    return "A"
  elif average >= 90:
    return "A-"
  elif average >= 87:
    return "B+"
  elif average >= 83:
    return "B"
  elif average >= 80:
    return "B-"
  elif average >= 77:
    return "C+"
  elif average >= 73:
    return "C"
  elif average >= 70:
    return "C-"
  elif average >= 67:
    return "D+"
  elif average >= 63:
    return "D"
  elif average >= 60:
    return "D-"
  else:
    return "F"