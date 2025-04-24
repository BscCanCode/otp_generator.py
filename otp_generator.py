#generating otp for the input to validate
import random
import string
phone_number=input("Enter your mobile number:")
if len(phone_number)==10 and phone_number.isdigit():
    otp=''.join(random.choices(string.digits,k=4))
    print("Your otp to login is:",otp)
    otp_input=input("Enter the 4 digit otp:")
    if otp==otp_input:
        print("Validated Successfully")
    else:
        print("Incorrect otp,not validated")
else:
    print("Phone number should be of 10 digits, greater than or less than 10 digits phone number are not accepted")
