# Define functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def mod(x, y):
    return x % y

# Main function for calculator logic
def calculator():
    print("Welcome to the Python Calculator!")
    while True:
        # Display available operations
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Exit")

        # Get user input for operation
        choice = input("Enter choice (1/2/3/4/5/6): ")

        # Check if the user wants to exit
        if choice == '6':
            print("Exiting calculator. Goodbye!")
            break

        # Check if the user input is valid
        if choice in ['1', '2', '3', '4', '5']:
            try:
                # Get numbers from the user
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                # Perform the chosen operation
                if choice == '1':
                    print(f"The result is: {add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result is: {divide(num1, num2)}")
                elif choice == '5':
                    print(f"The result is: {mod(num1, num2)}")

            except ValueError:
                print("Invalid input! Please enter numerical values.")
        else:
            print("Invalid choice! Please choose a valid operation.")
            
# Run the calculator function
calculator()
