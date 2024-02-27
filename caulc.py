from os import system, name
from time import sleep

#This is the "Clear" Function that gets used at the end of the caculate func so that we can clear the console
def clear():
    #windows
    if name == 'nt':
        _= system('cls')
    #for mac and linux (name is posix)
    else: 
        _ = system('clear') 

# The very end proment where we ask the user if we want to run the app again and if they say no exit the app or run the calculate func again
def again():
    calc_again = input('''
    Do you want to perform another opration?
    Please type Y for Yes or N for No.
    ''')
    goodbey = 'Thank you for useing my app (the app will now exit)'
    if calc_again == 'Y':
        clear()
        calculate()
    elif calc_again == 'y':
        clear()
        calculate()
    elif calc_again == 'N':
        print(goodbey)
    elif calc_again == 'n':
        print(goodbey)
    
    else:
        clear()
        again()

#This is the main app func it gets the users input for what opration they would like to perform then askes the user for 2 numbers and uses a if else statment to print the opration and calculates the 2 numbers based on the opration
def calculate():
    opration = input('''
    Please type in the oparation you would like to complete:
    + for addition
    - for subtration
    * for multiplaction
    / for division
    ''')

    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    if opration == '+':
        print('{} + {} ='.format(number_1, number_2), number_1 + number_2)
    
    elif opration == '-':
        print('{} - {} ='.format(number_1, number_2), number_1 - number_2)

    elif opration == '*':
        print('{} * {} ='.format(number_1, number_2), number_1 * number_2)

    elif opration == '/':
        print('{} / {} ='.format(number_1, number_2), number_1 / number_2)
    #wait 3 seconds
    sleep(3)
    #call the clear func to clear the consle
    clear()    
    #display the Run again? promt
    again()
calculate()
