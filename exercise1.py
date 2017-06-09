CURRENT_YEAR = 2017

def find_year_when_100(age):
    if age > 100:
        return -1
    else:
        return (100 - age) + CURRENT_YEAR

def create_response(yearWhenTurn100):
    if yearWhenTurn100 == "-1":
        return "You're Old!"
    else:
        return "Wow " + username + ", in the year " + yearWhenTurn100 + ", you'll be 100!!!"

username = input("Please Enter Your First Name: ")

userAge = int(input("Please Enter Your Age: "))

yearWhen100 = str(find_year_when_100(userAge))
print(create_response(yearWhen100))
