# Reading two numbers and dividing the first one by the second, and give the integer result and the remainder.

#program that reads in two numbers and outputs the integer answer and remainder

x = int (input ("Enter first number: "))
y = int (input ("Enter the number you want to divide it by: "))
answer = int (x//y)
remainder = x % y
print ("{} divided by {} is {} with remainder {}".format (x,y,answer, remainder))


