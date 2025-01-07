# Calculator menu
print ("Select an Operation to Perform:")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")

# Operation logic
def calculate ():
    operation = input ('Enter the number of operation from 1-4:')
    
    num_1 = int(input('please enter the first number:'))
    num_2 = int(input('input the second number:'))

    if operation == '1':
        print ('{} + {} = '.format(num_1, num_2))
        print(num_1 + num_2)
    elif operation == '2':
        print ('{} - {} = '.format(num_1, num_2))
        print (num_1 - num_2)
    elif operation == '3':
        print ('{} * {} ='.format(num_1, num_2))
        print (num_1 * num_2)
    elif operation == '4':
        if num_2 == 0:
            print ('Division by 0 is not allowed')
        else:
            print ('{} / {} = '.format(num_1, num_2))
            print (num_1 / num_2)
    else:
        print ('Please type a valid operation')

calculate ()


