print("I'll help you determine how long you will need to save.")
name = input("What is your name? ")
item = input("What is it you are saving for? ")

balance = float(input("OK, "+name+ ".  Please enter the cost of the "+item+ ": "))
if (balance < 0):
    print("Looks like you already have enough saved!")
    balance = 0
    payment = 1

else:
    payment = float (input("Enter how much you will save each month:"))
    if (payment <=0):
        payment = float(input("Savings must be positive. Please enter a positive value:"))
        if (payment <=0):
            print(name+", you still didnt enter a positive number!  I am going to just assume you save 1 per month.")
            payment = 1
# Calculate number of payments that will be needed

num_remaining_payments = int(balance/payment)
    if (num_remaining_payments < balance/payment):
        num_remaining_payments = num_remaining_payments + 1

# Present information to user

print(name, ", You must make", num_remaining_payments, "more payments, and then you'll have your ", item, "!")