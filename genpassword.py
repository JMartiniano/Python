# Import library of random
from random import randint

# How many digits password
tam = int(input('How many digist in the password? '))

# Array to save the passwords 
passwords = []

# How many passwords to generating
howmany = int(input('How many passwords to genarating? '))


writeYN = input('Do you want write the passwords on a .txt? [y,n] ')

if writeYN == "y" or writeYN == "Y":
    # Asking for the path
    path = input('Path to the file: ')
    # Opening the file
    arqpasswords = open(path, 'w')

#Asking about fomart
print (f'\nFormat option A:\n--------------\n[01] - password\n--------------\n[02] - password\n--------------\n')
print (f'\nFormat option B:\npassword\npassword\n')
optformat = input('Choice a format option: [A,B]')

print ('-' * (tam+(len(str(howmany)))+7))

# For that will create howmany random passwords with tam digits each
for i in range(howmany):
    
    # Generating passwords
    password = int(''.join(str(randint(0,9)) for _ in range(tam)))
    
    # Saving passwords in the array
    passwords.append(password)

    if writeYN == 'y' or writeYN == 'Y':

        if optformat == "b" or optformat == "B":
            
            # Writing the passwords
            arqpasswords.write(f"{str(passwords[i])}\n")        

        elif optformat == "a" or optformat == "A":
            arqpasswords.write(f"[{i+1:0>4}] - {passwords[i]:0>6}\n" + '-' * (tam+(len(str(howmany)))+7) + '\n')

    else:
        print (f"[{i+1:0>4}] - {passwords[i]:0>6}")
        print ('-' * (tam+(len(str(howmany)))+7))