import random

lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

def getRandomLower():
    return lowerCase[random.randint(0, len(lowerCase) - 1)]
def getRandomUpper():
    return upperCase[random.randint(0, len(upperCase) - 1)]
def getRandomNumber():
    return numbers[random.randint(0, len(numbers) - 1)]
def getRandomSymbol():
    return symbols[random.randint(0, len(symbols) - 1)]


charaterTypes = []

while True:
    try:
        askLength = int(input('How many characters would you like your password to have? '))
        break
    except ValueError:
        print('You need to enter a valid number to continue')
        

while True:
    try:
        askLower = str(input('Would you like a lower case letter in your password? Yes or no. '))
        if askLower.lower() in ['yes', 'no']:
            break
        else:
            print("Please provide either 'yes' or 'no,'")
    except ValueError:
        print("Please provide either 'yes' or 'no'")


while True:
    try:
        askUpper = str(input('Would you like an upper case letter in your password? Yes or no. '))
        if askUpper.lower() in ['yes', 'no']:
            break
        else:
            print("Please provide either 'yes' or 'no,'")
    except ValueError:
        print("Please provide either 'yes' or 'no'")


while True:
    try:
        askNumber = str(input('Would you like a number in your password? Yes or no. '))
        if askNumber.lower() in ['yes', 'no']:
            break
        else:
            print("Please provide either 'yes' or 'no'")
    except ValueError:
        print("Please provide either 'yes' or 'no'")


while True:
    try:
        askSymbol = str(input('Would you like a symbol in your password? Yes or no. '))
        if askSymbol.lower() in ['yes', 'no']:
            break
        else:
            print("Please provide either 'yes' or 'no'")
    except ValueError:
        print("Please provide either 'yes' or 'no'")

if askLower.lower() == 'yes':
    charaterTypes.append(getRandomLower)
if askUpper.lower() == 'yes':
    charaterTypes.append(getRandomUpper)
if askNumber.lower() == 'yes':
    charaterTypes.append(getRandomNumber)
if askSymbol.lower() == 'yes':
    charaterTypes.append(getRandomSymbol)

password = []

for i in range(askLength):
    password.append(charaterTypes[random.randint(0, len(charaterTypes) - 1)])

for i in password:
    print(i(), end = '')