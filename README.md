# Calculator-CLI
## Overview

The Calculator-CLI is a simple command-line interface (CLI) calculator program written in Python. It allows users to perform basic mathematical operations such as addition, subtraction, multiplication, and division interactively.

## Features

1. Addition

2. Subtraction

3. Multiplication

4. Division

## How It Works

1. The program displays a menu of operations for the user to choose from:

    1: Add

    2: Subtract

    3: Multiply

    4: Divide

2. The user inputs the operation they want to perform by entering the corresponding number (e.g., 1 for addition).

3. The program prompts the user to input two numbers for the calculation.

4. The program performs the selected operation and displays the result.

## Code Explanation

### Example Code Snippet

    print('{} + {} = '.format(num_1, num_2))

    print(num_1 + num_2)

The curly braces {} are placeholders for the values of num_1 and num_2.

The .format(num_1, num_2) method dynamically inserts the values into the placeholders.

This line shows the operation being performed (e.g., 5 + 3 =).

The next line calculates and prints the result (e.g., 8).

## Requirements

Python 3.6 or later

## How to Run the Program

1. Clone or download the repository to your local machine.

        git clone https://github.com/Patricia-Sigei/Calculator-CLI.git

2. Navigate to the project directory using your terminal.

        cd Calculator-CLI

3. Open your Code Editor while in the Calculator-CLI directory by running the following command 

        code .

4. Run the following command:

        python main.py

Follow the on-screen instructions to perform calculations.

## Example Usage

Select an Operation to Perform:
1. Add
2. Subtract
3. Multiply
4. Divide

Enter the number of the operation (1-4): 1
Please enter the first number: 5
Please enter the second number: 3
5 + 3 = 
8

## Future Improvements

1. Add support for more operations (e.g., factorial).

2. Add support for more than two numeric values.

## License

This project is open-source and available under the MIT License.