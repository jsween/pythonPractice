CURRENT_YEAR = 2017

def get_user_age():
    isInteger = False
    while (not isInteger):
        userAge = input("Please Enter Your Age: ")
        isInteger = represents_int(userAge)
        if (isInteger == True):
            return int(userAge)
        else:
            print("Please insert a valid age.")

def get_fav_num():
    isInteger = False
    while (not isInteger):
        favNum = input("Please Enter Your Favorite Number: ")
        isInteger = represents_int(favNum)
        if(isInteger == True):
            return int(favNum)
        else:
            print(favNum + " is not authorized to be a favorite number!!!\nPlease try again...")

def print_output_fav_num_times(numTimes):
    for x in range(numTimes):
        print(create_response(yearWhen100))

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


username = input("Please Enter Your First Name: ").capitalize()
userAge = get_user_age()
favNum = get_fav_num()

yearWhen100 = find_year_when_100(userAge)
print_output_fav_num_times(favNum)
