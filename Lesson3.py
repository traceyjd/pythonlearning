#If Else True False
# Constant values have capital letter
x = int(input("What is your age?"))
x = (x <= 12)
if x:
    print("Your meal is free!")
else:
    print("Sorry, you are too old and have to pay.")


a = int(input("Enter a value for a:"))

#If this said lower case true this would be read by python as a variable!!!
#You have to Capitalise Constants
#After the word True we have a colon, this indicates we are going to see what happens if this condition were True
if True:
    print("Turning on the heating.")

#Remember to indent code, its very important to let the computer know where a new block of code begins, if using
#a basic text editor indent 4 spaces!!!

if True:
    print("Dangerous cholesterol levels!")

if True:
    print("Turning on the heating.")
    print("It was too cold")

if False:
    print("Turning on the heating.")
    print("It was too cold")
#The code above will all be printed to screen as both lines are indented
if False:
    print("Turning on the heating.")
print("It was too cold")
#the code above will print out the second line as this hasnt been indented so its executed if the condition is false

#by default all the code should be done True then false else it will never be true
if True:
    print("Turning on the heating.")
else:
    print("Temperature is fine.")
#The above code prints out the first line if the condition is true

if False:
    print("Turning on the heating.")
else:
    print("Temperature is fine.")
#The above code prints out the second line if the condition is false

if True:
    print("Dangerous cholesterol levels.")
else:
    print("Cholesterol levels seem ok")

# nesting conditions - overall statement is the the nest, the rest are inside the nest
if True:
    print("It is cold")
    if True:
        print("The heater is already on.")
    else:
        print("Turning the heater on.")
else:
    print("It is warm enough.")

#
if True: # called the outer statement
    if True: # called the inner statement or the nested statement
        if True:
            #do something
        else:
            #do something
    else:
        #do something
else:
    if True:
        #do something
    else:
        #do something



#Boolean Type of variable that can be either true or false

temp_is_low = True
if temp_is_low:
    print("Turning on the heater.")
else:
    print("Temperature is fine.")

a = 1
b = 2
c = 2

a > b  #False
a < b  #True
a >= b #False
a <= b #True
#notice the syntax the greater than or less than sign always comes first before the equals sign

#equal and not equal
#to compare for equality we use a == double equals sign - remember a single equals sign is an assignment

#remember a command performs an action, such as assigning a value to a variable
#whereas an expression is something that gets evaluated to find a value
# the interpreter will normally catch this for you if you get them mixed up
# != to compare for inequality

a = 1
b = 2
c = 2

a == b #False
a != b #True
b == c #True
a != b #


#If Else True False
# Constant values have capital letter
x = int(input("What is your age?"))
x = (x <= 12)
if x:
    print("Your meal is free!")
else:
    print("Sorry, you are too old and have to pay.")
# an easier way to do the code above is

age = int(input("What is your age?"))
if age <= 12:
    print("Your meal is free!")
else:
    print("Sorry, get your cash out you have to pay.")

# elif
if (age < 3):
    price = 0.00
else:
    if (age <-12):
        price = 10.00
    else:
        if  (age >= 65):
            price = 15.00
        else:
            price = 25.00
# more efficient way than above
if (age <3):
    price = 0.0
elif (age <=12):
    price = 10.00
elif (age >= 65):
    price = 15.00
else:
    price = 25.00

# For game of craps you can combine the losing and winning statements onto 1 line

if ((die1 + die2) ==2) or ((die1 + die2) == 3) or ((die1 + die2) == 12):
    win = False
elif ((due1 + die2) == 7) or ((die1 + die2) ==11):
    win = True
else:
    point = die1 = die2








