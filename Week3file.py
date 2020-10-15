# a= 1 
# b=2 
# c = a+b
# print(c)

#value = 4 % 5

#print(value) # Prints 0 (Therefore 10 is evenly divisible by 5)

# """
#     =========== Exercise 1 =============

#     I have provided some starter code below
#     that creates a result variable, and a number_1
#     variable. Your goal is to make number_1 equal 11
#     after the operations that have been done to it.
# """
# result = 0
# number_1 = 5
# number_1 += 52

# # Do more operations on number 1 until it equals eleven
# number_1 -= 46
# result = number_1
# print(result == 11)


# """
#     =========== Exercise 2 =============

#     Take input from the command line, and convert it to
#     an int. Now pick a range (i.e. 0-10), and create a set
#     of conditional statements that prints the string
#     representation of the number input by the user.

#     For example if someone put in 8, then it would print 'eight'.
    
#     Hint: Use if, elif and else statements.


val = input ("Enter Number between 1 and 10 ")
if(int(val) == 1):
    print ("One")
elif (int(val) == 2):
    print ("Two")
elif (int(val) == 3):
    print ("Three")
elif (int(val) == 4):
    print ("Four")
elif (int(val) == 5):
    print ("Five")
elif (int(val) == 6):
    print ("Six")
elif (int(val) == 7):
    print ("Seven")
elif (int(val) == 8):
    print ("Eight")
elif (int(val) == 9):
    print ("Nine")
elif (int(val) == 10):
    print ("Ten")
   
else:
    print ("out of bounds value")

print (val)


number = 0
number += 15
number //= 2
number *= 6
number -= 4

if number < 10:
    print("Less than 10")

elif 10 <= number <= 20:
    print("Between 10 and 20")

elif 20 <= number <= 30:
    print("Between 20 and 30")

elif 30 <= number <= 40:
    print("Between 30 and 40")

else:
    print("¯\_(ツ)_/¯")