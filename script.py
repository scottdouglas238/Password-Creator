import random


numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']
lowerCaseLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperCaseLetters = []
for letter in lowerCaseLetters:
    upperCaseLetters.append(letter.upper())


characterTypes = [numbers, lowerCaseLetters, upperCaseLetters, symbols]


def randomCharacters(password):
    randomIndex = random.randrange(4)
    randomCharacterType = characterTypes[randomIndex]

    if randomCharacterType == numbers or randomCharacterType == symbols:
         ChTindex = 10
    else:
         ChTindex = 26

    randomCharacterIndex = random.randrange(ChTindex)
    characterValue = randomCharacterType[randomCharacterIndex]
    return password + characterValue
    

    
    # print(characterValue)

# randomCharacters()


def createPassword():
    # passwordLength = 10
    password = '' 
    passwordLength = int((input('How many characters do you want your password to be?')))
    for i in range(passwordLength):
        password = randomCharacters(password)
        
    print(password)


    

createPassword()