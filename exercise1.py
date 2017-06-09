CURRENT_YEAR = 2017

def get_user_age():
    isInteger = False
    while (isInteger == False):
        userAge = input("Please Enter Your Age: \n")
        isInteger = represents_int(userAge)
        if (isInteger == True):
            return int(userAge)
        else:
            print("Please insert a valid age.")


def represents_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

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
userAge = get_user_age()

yearWhen100 = find_year_when_100(userAge)
print(create_response(yearWhen100))
