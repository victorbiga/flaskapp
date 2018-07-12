#Ask the user to input 2 values and store them in #variables num1 num2
#convert the strings into regular numbers Integer
num1, num2 = input('Enter 2 numbers: ').split()
#Add the values entered and store in sum
num1 = int(num1)
num2 = int(num2)

# Sumbtract values and store in difference
sum = num1 - num2
#Multiply the values and store in product
product = num1 * num2
#Divide the values and store in quotient
quotient = num1 / num2
#Use modules on the values to finds the remainder
remainder = num1 % num2
#Print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} + {} = {}".format(num1, num2, product))
print("{} + {} = {}".format(num1, num2, quotient))
print("{} + {} = {}".format(num1, num2, remainder))

