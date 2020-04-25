'''
Created on Apr 24, 2020

@author: ITAUser
'''

def sum_three_numbers(num1, num2, num3):
    sumOfNums = num1 + num2 + num3
    return sumOfNums

sum_three_numbers (4, 5, 8)

x = sum_three_numbers(4, 5, 8)

print(x)



def taxCalc(subTotal, tax):
    taxAmount = subTotal * tax
    total = subTotal + taxAmount
    shipping = 0
    
    if(total > 100): 
        shipping = 0 
    elif(total > 50):
        shipping = 10
    else:
        shipping = 5
        
    total = total + shipping
    return total

y = taxCalc(152, .05)

print(y)

y = taxCalc(80, .05)

print(y)

y = taxCalc(10, .05)

print(y)

def capFirstName(name):
    name = name[0].upper() + name[1:]
    return name

z = capFirstName("Caleb")
print(z)









