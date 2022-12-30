######  Lists #####

# When creating lists in python remember the first box is 0 and not 1 ######

daily_high_temps = [83,80,73,75,79,83,86]
print(daily_high_temps[3])
print(daily_high_temps[1])
print(daily_high_temps[3])
print(daily_high_temps[5])
i = 1
print(daily_high_temps[i])

# How to change a value in a list
daily_high_temps = [83,80,73,75,79,83,86]
daily_high_temps[3]=100
print(daily_high_temps[3])

# change february to 29
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(days_in_month[0])
print(days_in_month[1])
(days_in_month[1]) = 29
print(days_in_month[1])

# Account for a leap year
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 2020
# use "%" to calculate the remainder from division
if (year%4 == 0):
    days_in_month[1] = 29
print(days_in_month[1])

#  How to print out all elements of a list
daily_high_temps = [83,80,73,75,79,83,86]
for i in range(7):
    print(daily_high_temps[i])

daily_high_temps = [83,80,73,75,79,83,86]
x = len(daily_high_temps)
print(x)

daily_high_temps = [83,80,73,75,79,83,86]
for i in range(len(daily_high_temps)):
    print(daily_high_temps[i])

daily_high_temps = [83,80,73,75,79,83,86]
for i in daily_high_temps:
    print(i)

#  The following code will set all the elements to 0
daily_high_temps = [83,80,73,75,79,83,86]
for i in range(7):
    daily_high_temps[i]=0
    print(daily_high_temps[i])

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num_days = 0
for i in range(12):
    num_days += days_in_month[i]
    print(num_days)

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num_days = 0
for i in range(len(days_in_month)):
    num_days += days_in_month[i]
    print(num_days)

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num_days = 0
for i in days_in_month:
    num_days += i
    print(num_days)

#  Command in python called sum to calculate all the values in the list as follows

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num_days = sum(days_in_month)
print(num_days)

# Actions for lists
#  Appending
#  Indexing
#  Slicing
#  Lists of lists

list1 = [3.1, 1.2, 5.9]
list2 = [3.0, 2.5]
list3 = list1 + list2
print(list1)
print(list2)
print(list3)

#  or appending a list to the end of the first list
list1 = [3.1, 1.2, 5.9]
list2 = [3.0, 2.5]
list1 += list2
print(list1)
print(list2)

#  appending to a current list
list1 = [3.1, 1.2, 5.9]
print(list1)
list1.append(3.9)
print(list1)


ages = []
age = int(input("Enter an age of a group member. Enter -1 when done"))
#  operators "!=" means "does not equal"

while(age != -1):
    ages.append(age)
    age = int(input("Enter an age of a group member.  Enter -1 when done"))
    print(ages)



##  If you try and print out a element from a list thats out of range you get the following error.  The list has 7 items and we are trying
##  to print out element 8
## IndexError: list index out of range

daily_high_temps = [83,80,73,75,79,83,86]
print(daily_high_temps[8])

##  Teh following will print out the last number in the list and the last 3rd number
daily_high_temps = [83,80,73,75,79,83,86]
print(daily_high_temps[-1])
print(daily_high_temps[-3])

##  Slicing
##  varname[a:b]  The first value a is the starting value for your slice and the second value is the number you want to stop before

daily_high_temps = [83,80,73,75,79,83,86]
##  The following prints the first 3 elements
print(daily_high_temps[0:3])
##  The following prints elements 4 and 5
print(daily_high_temps[4:6])
##  The following prints the first 4 elements
print(daily_high_temps[:4])
##  The following prints the last 3 elements
print(daily_high_temps[-3:])
##  The following prints the all the elements of the list
print(daily_high_temps[:])