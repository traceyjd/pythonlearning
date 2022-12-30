#Basic development and testing

# Get information from user
balance = float (input("Enter how much you want to save! "))
if (balance < 0):
    print("Looks like you already have enough saved!")
    balance = 0

payment = float (input("Enter how much you will save each month:"))

if (payment <=0):
    payment = float(input("Savings must be positive. Please enter a positive value:"))

print("Balance is", balance, "and payment is", payment)

# Calculate number of payments that will be needed

num_remaining_payments = balance/payment

# Present information to user

print("You must make", num_remaining_payments, "more payments.")

# modified version of above

balance = float (input("Enter how much you want to save! "))
if (balance < 0):
    print("Looks like you already have enough saved!")
    balance = 0
    payment = 1

else:
    payment = float (input("Enter how much you will save each month:"))
    if (payment <=0):
        payment = float(input("Savings must be positive. Please enter a positive value:"))

# Calculate number of payments that will be needed

num_remaining_payments = balance/payment

# Present information to user

print("You must make", num_remaining_payments, "more payments.")