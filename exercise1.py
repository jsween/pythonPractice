def years_until_100(age):
    if age > 100:
        return -1
    else:
        return 100 - age

def create_response(yearsTo100):
    if yearsTo100 == -1:
        return "You're Old!"
    else:
        return "Less than " + yearsTo100 + " years until you're 100!!!"

username = input("Please Enter Your First Name: ")

userAge = int(input("Please Enter Your Age: "))

yearsTo100 = str(years_until_100(userAge))
print(create_response(yearsTo100))
