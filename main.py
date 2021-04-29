# and shoot for the Sky in you getting a big promotion & opportunity
# Enter Full Names
print("Enter First and Last Name:")
firstname = input("Enter First Name")
lastname = input("Enter Last Name")
fullname = firstname + " " + lastname


# Enter phone, email
print("Enter Customer's Phone Number")
phone = input("phone")
print("Enter Customer's email address")
email = input("Email")

# price of a used car
price = 10000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down Payment: {down_payment}")
print('')
print("Full Names:" + fullname)
print("Phone: " + phone)
print("Email: " + email)
print("Down Payment:" + str(down_payment))