import string
import random

#function to ensure there is at least one digit present in the password
def checkNum (s):
    return any(i.isdigit() for i in s)

def passwordgenerator (length) :
    ##empty string for password 
    password = ''
    l = int(length)

    #list of charcters to choose from
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    
    #generate random password from the list of characters  
    for x in range(l):
        password = password + (random.choice(chars))
    
    check = checkNum(password)

    test = random.choice(string.digits)
    print(test)

    #check if there is at least a number present in the generated password
    if check == True :
        print('Your password is : ',password)

    #if no number is present, add a number at a random position and shuffle the arrangement of the characters
    else :
        print('here')
        i = random.randint(0,len(password))
        new = list(password)
        new[i] = random.choice(string.digits)
        random.shuffle(new)
        password = ''.join(new)
        print('Your password is : ',password)


    
            
def main ():
    print('\n\t\t Welcome to the password generator system')
    print('\t\t Password length can vary from length 8 to 15')
    print('\t\t The minimum recommended length is a length of 10')
    
    #ensuring the input is a number and is between 8 and 15
    while True :
        length = input("\n Type in the desired length of password in digits: ")

        if (length.isnumeric() == True and int(length) >= 8 and int(length) <= 15):
            passwordgenerator(length)
            break

        else :
            print('please enter in a value between 8 and 15 in digits')
            

main ()