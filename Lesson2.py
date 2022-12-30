first_name = "Tracey"
last_name = "Doherty"
full_name = first_name + " " + last_name
print (full_name)

#The print command will print once space for each comma when it displays the results

#New Name
name = input("What is your name?")
print("Hi,", name)

a = "John"
b = 3.14159
c = 100
print(a,b,c)
#commas below add an additional space between or after words
print("Hello","\n","World")
print("Hello"+"\n"+ "World")
print(b+c)

# Constant values have capital letter
x = int(input("What is your age?"))
x = (x <= 12)
if x:
    print("Your meal is free!")
else:
    print("sorry, you have to pay.")

#address
city_name = "Livingston"
country = "Scotland"
post_code = "EH54 9JU"
address = city_name + "\n" + country + "\n" + post_code
print (address)


a = int(input("Enter a value for a:"))

#Notes
#All input comes in as a string

interest_rate = 0.03
principal = 2000
interest_earned = interest_rate * principal
total_amount = principal + interest_earned
print (total_amount)

#New name
name = input("What is your name?")
print("Hi,", name)

#New Line
print ("Hello"+"\n"+"World")

#Fav Colour
Question3 = input('What is your favourite colour?')
print(Question3)
b = input()
print('You entered', b)

#String/Concat
a = (input("Enter a value for a:"))
b = (input("Enter a value for b:"))
print("The sum of a and b is ", a+b)

#Int/Concat
a = int(input("Enter a value for a:"))
b = int(input("Enter a value for b:"))
print("The sum of a and b is ", a+b)

#Data is always input as a string!!!!!!!!

#Bank Balance
balance = 1000.00
withdrawal_amount = 20.00
#
#balance = balance - withdrawal_amount
# or
balance -= withdrawal_amount
print (balance)

# y = 5
# y += 1 - increases by 1
# z = 8
# z -= 1 - decreases by 1
# m = 1-
# n = 10
# m *= 2 - multiply by 2
# n /= 2 - divide by 2


radius = float(input("Enter the radius:"))
pi = 3.14159
area = pi * radius * radius
print ("The area is:", area)

#Or you can concatinate the area with the text, but to concatinate you need two strings, so since area is a
# float you have to convert it to a string first!!!
radius = float(input("Enter the radius:"))
pi = 3.14159
area = pi * radius * radius
print ("The area is:" + str(area))

