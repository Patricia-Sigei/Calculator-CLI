# Calculator menu
# print ("Select an Operation to Perform:")
# print ("1. Addition")
# print ("2. Subtraction")
# print ("3. Multiplication")
# print ("4. Division")

# class Operation:
#     def _init_ (self, addition, subtraction, multiplication, division):
#             self.addition = addition
#             self.subtraction = subtraction
#             self.multiplication = multiplication
#             self.division = division

# # Operations = [
# {"addition" : "-"},
# {"subtraction" : "-"},
# {"multiplication" : "*"},
# {"division" : "/"},
# {"exponent" : "**"}
# ]

# def calculate():
#     operations = ["parenthesis", "exponent", "multiply", "divide", "addition", "subtraction"]
    
#     while True:
#         operation = input("Enter Operation")
    
#         numbers = []
#         while True:
#                 num = int(input("Enter a number"))
#                 numbers.append(num)
        
#         if operation == "addition":
#             result = sum(numbers)
#         elif operation == "subtraction":
#             result = numbers[0]
#             for num in numbers[1:]:
#                 result -= num
#         elif operation == "multiply":
#             result = 1
#             for num in numbers:
#                 result *= num
#         elif operation == "divide":
#             result = numbers[0]
#             for num in numbers[1:]:
#                 result /= num
#         elif operation == "exponent":
#             result = numbers[0]
#             for num in numbers[1:]:
#                 result **= num


# calculate()




# # Operation logic
def calculate():
    operation = input('Enter the number of operation (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): ')
    numbers = input('Enter the numbers separated by spaces: ').split()
    numbers = [float(num) for num in numbers]

    if operation == '1':
        result = sum(numbers)
        print(f"The result of adding {numbers} is: {result}")
    elif operation == '2':
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        print(f"The result of subtracting {numbers} is: {result}")
    elif operation == '3':
        result = 1
        for num in numbers:
            result *= num
        print(f"The result of multiplying {numbers} is: {result}")
    elif operation == '4':
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
            print(f"The result of dividing {numbers} is: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
    else:
        print('Please type a valid operation')

calculate()



