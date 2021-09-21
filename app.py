import addition
import division
import multiplication
import subtraction


keepRunning = True

while keepRunning:
    print ("Select an operation below")
    print ("1 = Add")
    print ("2 = Subtract")
    print ("3 = Multiply")
    print ("4 = Divide")

    user_choice = input("Enter your operation choice (1, 2, 3, or 4): ")

    if user_choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Thats not a number... how can I operate this way?!")
            else:
                if (user_choice == "1"):
                    print(num1, "+", num2, "=", addition.add(num1, num2))
                elif (user_choice == "2"):
                    print(num1, "-", num2, "=", subtraction.subtract(num1, num2))
                elif (user_choice == "3"):
                    print(num1, "*", num2, "=", multiplication.multiply(num1, num2))
                elif (user_choice == "4"):
                    if(num2 == 0):
                        print("You cannot divide by 0, try again")
                        num2 = float(input("Enter second number: "))
                        if (num2 == 0):
                            print("You don't listen..Goodbye")
                            keepRunning = False
                            break
                    print(num1, "/", num2, "=", division.divide(num1, num2))

                start_again = input("Would you like to calculate again? (Y/N):  ")
                if(start_again == "Y" or start_again == "y"):
                    keepRunning = True
                elif(start_again == "N" or start_again == "n"):
                    print("GoodBye!")
                    keepRunning = False
                else: 
                    print("I didnt understand that, you dont listen well.. So Goodbye!")
                    keepRunning = False  
    else:
        print("Invalid Choice")    