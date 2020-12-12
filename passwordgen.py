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
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    

    for x in range(l):
        password = password + (random.choice(chars))
    
    check = checkNum(password)

    if check == True :
        print('Your password is : ',password)

    else :
        i = random.randint(0,len(password))
        password[i] = random.choice(string.digits)
        random.shuffle(password)
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
            print('please enter in a value between 8 and 15')
            

main ()
