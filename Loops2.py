# A while loop is used when we are not sure how many times we will need to iterate through the loop

a = 0
while a < 3:
    print (a)
    a = a+1
# 1 time through a loop is called an iteration

value = 10
while value > 0:
    print(value)
    value -= 1

#
num_people = int (input("How many people are there? "))
i = 0
total_age = 0.0
while (i < num_people):
    age = float(input("Enter the age of person" +str(i+1)+ ":"))
    total_age = total_age + age
    i = i+1
average_age = total_age / num_people
print("The average age was", average_age)

# for loop is used when we have a precise set of things to loop through, or know how many times to iterate
for i in range (4):
    print(i)

# Range commands
# One value listed in (), start at 0 and increment by 1, not exceeding the value in ()
# Two values listed in (), increment by 1 starting from the first value and not exceeding the second value
# Three values listed in (), start value, limit, increment amount

for i in range (0, 7, 1):
    print(i)

for i in range (1, 7, 2):
    print(i)

for i in range (5, 1, -1):
    print (i)

i = 5
while i > 1:
    print(i)
    i = i - 1

# For the while loop, the condition being true will do the main part of the body, when condition is false it will do the else statement
while value <= 0:
    value = int(input("Enter a positive value!"))
else:
    print("You entered", value)

for i in range (10):
    for j in range (10):
        print(i, '*', j, '=', i*j)

for i in range (1, 11):
    for j in range (1, 11):
        print(i, '*', j, '=', i*j)

#or
for i in range (10):
    for j in range (10):
        print(i+1, '*', j+1, '=', (i+1) * (j+1))

#
numpeople = int(input("How many people are there?"))
for i in range(1, numpeople+1):
    for j in range (i+1, numpeople+1):
        print(i, j)

# loop for odd and evens
n = int(input("Enter a number: "))
print(n)

count = 0

while n !=1:
    count += 1
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n+1
    print("We reached 1 in", count, "steps.")

n = int(input("Enter a number: "))
print(n)


##########
count = 0

while n !=1:
    count += 1
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n+1
    print("We reached 1 in", count, "steps.")