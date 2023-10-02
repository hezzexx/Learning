# NOTE, this has a weird bug where it just spams 'This is not valid! Please Try Again', although it will still work

dmas = input('Choose between division (D), multiplication (M), addition (A), and subtraction (S) (MUST BE '
             'CAPITALIZED): ')

if dmas == 'A':
    first_number = input('1st Number: ')
    second_number = input('2nd Number: ')
    total = int(first_number) + int(second_number)
    print('Total: ' + str(total))
else:
    print("This is not valid! Please try again!")
if dmas == 'D':
        first_number = input('1st Number: ')
        second_number = input('2nd Number: ')
        total = int(first_number) / int(second_number)
        print('Total: ' + str(total))
else:
 print("This is not valid! Please try again!")

if dmas == 'M':
    first_number = input('1st Number: ')
    second_number = input('2nd Number: ')
    total = int(first_number) * int(second_number)
    print('Total: ' + str(total))
else:
    print("This is not valid! Please try again!")

if dmas == 'S':
    first_number = input('1st Number: ')
    second_number = input('2nd Number: ')
    total = int(first_number) - int(second_number)
    print('Total: ' + str(total))
else:
    print("This is not valid! Please try again!")
