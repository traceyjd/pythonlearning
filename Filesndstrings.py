# Read input from MyDataFile.txt
# Write output to results.txt

infile = open("MyDataFile.txt", "r")
outfile = open("results.txt", "w")

# how to close a file - myfile.close()

#### OPTION 1
myfile = open("Filename", "w")
# Do something here
myfile.close()

#### OPTION 2 ONLY OPEN FOR SECTION INDENTED
with open("Filename", "w") as myfile:
    # Do something here

# how to close your files
infile = open("MyDataFile.txt", "r")
outfile = open("results.txt", "w")
# DO STUFF HERE
outfile.close()
infile.close()

# How to write to a file - ****WE CAN ONLY WRITE OUT STRINGS****
# Can only write one string at a time
# Does not put in a new line character at the end of each line you write
# You must explicitly write out a new line with \n
myfile = open("Filename", "w")

myfile.write("This line is written to the file.")

myfile.close()

myfile = open("Filename", "w")

myfile.write("The number of countries is: " + str(196))

myfile.close()

# Assume the variables "volume1" and "volume2" have been computed with open("results.txt", "w") as outfile:
    outfile.write("The first volume is " + str(volume1) + '\n')
    outfile.write("The second volume is " + str(volume2) + '\n')

#  Reading lines from a file
myfile = open("Filename", "r")
linefromfile = myfile.readline()
secondline = myfile.readline()
myfile.close()

# How to read in and read out to file
myfile = open("Filename", "r")
outfile = open("output.txt", "w")
linefromfile = myfile.readline()
secondline = myfile.readline()
outfile.write(linefromfile)
outfile.write(secondline)
outfile.close()
myfile.close()

##########
myfile = open("Filename", "r")

linefromfile = myfile.readline()
while linefromfile != "":
    # do something here
    linefromfile = myfile.readline()
myfile.close()

# easier way to do the above using python
myfile = open("Filename", "r")

for linefromfile in myfile:
    # do something

myfile.close()
########
# Generally when you read a file its 1 line at a time but its not the only thing you can do.
# You can read in a full file as a string using the following: you can then break the string into smaller strings by dividing it up into lines
myfile = open("Filename", "r")

linefromfile = myfile.read()

myfile.close()

##########
#### Remember you can only read in text files ####
# To write to a binary file
myfile = open("Filename", "wb")

# to append to a binary file
myfile = open("Filename", "ab")

# to read a binary file
myfile = open("Filename", "rb")

# Pickle module is available to help you with binary files

# Directory structure
# C:\Users\Tracey\PyCharmProjects (Windows)
# /Users/Tracey/PyCharmProjects (Mac)
# /usr/local/bin - Python Commands
#  ../..Programming (Mac)
#  ..\..Programming (Windows)

#  Mac OS X
infile = open('data/data.txt', 'r')

#  Windows
infile = open('data\\data.txt', 'r')  # \\ only used for strings specified in the program

# Use the Escape \ to specify your using quotes inside quotation marks
\': string
\": string
\n: new line character
\t: tab
\\: escape character for the \ (backslash)

"""Three quotes in a row will begin a new string and let it continue
new lines and al, until the matching three quotes are encountered"""

'''Three quotes in a row will begin a new string and let it continue
new lines and al, until the matching three quotes are encountered'''









