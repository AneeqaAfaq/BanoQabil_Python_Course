#ANEEQA AFAQ
#aneeqaafaq@gmail.com
# A Python calculator with a simple command-line interface. It supports basic arithmetic operations like addition, subtraction, multiplication, and division. The user can input mathematical expressions, and the calculator evaluates and displays the results. Error handling is implemented to handle invalid inputs gracefully.

print("~~~~~Calculator~~~~~")

# I write flaot here because  float is necessary for division.

num1 = float(input("Enter first number here: "))
num2 = float(input("Second number here: "))

# Here I have given the users the choice to do addtion, substraction, multiplication or division, and we will print the result.

print("press 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress 4 for division ")

# Here we will take the value as an integer here because we cannot have a choice value in points or decimal.
# And you have to enter the choice 1 till 4 .

choice = int(input("Enter your choice from 1-4: "))

# here we are going to give conditional statement.
if choice == 1:
      print("The addtion of given two number is" ,num1 + num2) # If we choose 1 here it will perform addtion
elif choice == 2:
     print("The substraction of given two number is" ,num1 - num2) # If we choose 2 here it will perform substraction.
elif choice == 3:
    print("The multiplication of given two number is " ,num1 * num2) # If we choose 3 here it will perform multiplication.
elif choice == 4:
     print ("The division of given two number is" ,num1 / num2) # If we choose 4 here it will perform division.
else:
    print("Invalid input") # If we write a number other than 1-4, it will considered as invalid input.