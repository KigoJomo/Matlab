1. Initial Setup:
   - `ch = 0` initializes a variable `ch` (choice) to 0

2. Main Loop:
   - `while ch < 5` starts a loop that continues as long as `ch` is less than 5
   - This means the program will keep running until the user selects option 5 (Exit)

3. Display Interface:
   - Prints a line of dashes as a separator
   - Displays the program title and instructions
   - Asks user to enter two numbers

4. Input Collection:
   - `a = int(input("Enter first number: "))` gets the first number from user
   - `b = int(input("Enter second number: "))` gets the second number
   - Both inputs are converted from strings to integers using `int()`

5. Menu Display:
   - Shows the available operations (1-5)
   - Gets user's choice with `ch = int(input('> '))`

6. Operation Selection:
   - Uses if/elif statements to perform the chosen operation:
     - If `ch == 1`: Adds numbers (`a + b`)
     - If `ch == 2`: Subtracts numbers (`a - b`)
     - If `ch == 3`: Multiplies numbers (`a * b`)
     - If `ch == 4`: Divides numbers (`a / b`)
     - If `ch == 5`: Prints exit message and breaks the loop
     - If none of above: Prints "Invalid choice" message

7. Loop Continuation:
   - After each operation, prints another separator line
   - Returns to start of loop unless user chose to exit (option 5)

For example, if you run this program and:
1. Enter first number: 10
2. Enter second number: 5
3. Choose operation 1 (Add)
The program will output: "Result: 15"
Then it will loop back to the beginning for another calculation unless you choose to exit.