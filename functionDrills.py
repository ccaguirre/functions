'''
Created on Apr 24, 2020

@author: ITAUser
'''
#1) Define a function that subtracts the second number from the first number. Return the result.

def difference_two_numbers(num1, num2):
    differenceOfNums = num1 - num2
    return differenceOfNums

difference_two_numbers(10, 5)

x = difference_two_numbers(10, 5)

print(x)

#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def divide_multiply_add(num1):
    sumOfNums = ((num1/2) * 77) + 10000
    return sumOfNums

divide_multiply_add(100)

z = divide_multiply_add(100)

print(z)



#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def test_number1(x, y):
    if x == y:
        return True
    else:
        return False

  
#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should j return that number.
def function_max(a, b):
    if a > b:
        return a
    if a < b:
        return b
    elif a == b:
        return a
        

#5) Define a function that takes in two words and returns a string that contains both words combined.
def combine_text(string1, string2):
    string  = (string1 + string2)
    return string 
        
#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def three_numbers(num1, num2, num3):
    if num1 == (num2 or num3):
        return True
    else:
        return False
#7) Define a function that prints your name.
def my_name(num5):
    if num5 == num5:
        return "Caleb"

#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
def fav_color(string1):
    if(string1=="purple"):
        return print("thats my favorite color!")
    else:
        return print("That's not my favorite color. Try Again.")
#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def zero(num1):
    if num1 == 0:
        return True




#10) Create your own function that solves any problem you can think of.

def my_function(dog1, dog2,):

    my_function(dog1 ="Dewey", dog2 = "Stella")
    
    print("The youngest dog is " + dog2)



