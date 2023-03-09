#Nicolas Ibanez Delgado
from decode import *
loop = True 

def encode(password):
    my_str = ''
    for i in range(len(password)):
        curr_num = int(password[i])
        curr_num += 3
        my_str +=  (str(curr_num))
    password = my_str
    return password



while loop == True:
    print('Menu\n------------- \n1. Encode\n2. Decode\n3. Quit')
    menu = int(input("Please enter an option: "))
    if menu == 1:
        password = input('Please enter your password to encode: ')
        encode(password)
        print( "Your password has been encoded and stored!")
        continue
    elif menu == 2: 
        print(decode("45678888"))
        #print (f'The encoded password is {encode(password)}, and the original password is {password}.')
        continue
    elif menu == 3:
        break
