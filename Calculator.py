dma = input('Choose between division (D), multiplication (M), and addition! (A) (MUST BE CAPITALIZED): ')

if dma == 'A':
    first_number = input('1st Number: ')
    second_number = input('2nd Number: ')
    total = int(first_number) + int(second_number)
    print('Total: ' + str(total))
else:
    print("This is not a valid! Please try again!")
if dma == 'D':
        first_number = input('1st Number: ')
        second_number = input('2nd Number: ')
        total = int(first_number) / int(second_number)
        print('Total: ' + str(total))
else:
 print("This is not a valid! Please try again!")

if dma == 'M':
    first_number = input('1st Number: ')
    second_number = input('2nd Number: ')
    total = int(first_number) * int(second_number)
    print('Total: ' + str(total))
else:
    print("This is not a valid! Please try again!")