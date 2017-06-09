CURRENT_YEAR = 2017

def find_year_when_100(age):
    if age < 100:
        return (100 - age) + CURRENT_YEAR
    elif age > 100:
        return CURRENT_YEAR - (age - 100)
    else:
        return CURRENT_YEAR

def create_response(yearWhenTurn100):
    if yearWhenTurn100 > CURRENT_YEAR:
        return "Guess what " + username + ", in the year " + str(yearWhenTurn100) + ", you'll be 100!!!"
    elif yearWhenTurn100 < CURRENT_YEAR:
        return "You're old " + username + "! In " + str(yearWhenTurn100) + ", you turned 100!!!"
    else:
        return "Congratulations " + username + "!!! This is the year you turn 100!!!"


username = input("Please Enter Your First Name: \n").capitalize()

userAge = int(input("Please Enter Your Age: \n"))

yearWhen100 = find_year_when_100(userAge)
print(create_response(yearWhen100))
