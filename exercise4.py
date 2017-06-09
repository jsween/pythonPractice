def check_if_num(string):
    isInteger = False
    isGreaterThan2 = False
    while not (isInteger and isGreaterThan2):
        num = input(string)
        isInteger = represents_int(num)
        if(isInteger):
            isGreaterThan2 = check_if_greater_than_2(num)
        if(isInteger and isGreaterThan2):
            return int(num)
        else:
            print("Life is hard huh?  Please enter a valid number.\n")

def represents_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def get_user_num():
    string = "Please enter a number greater than 2: "
    return check_if_num(string)

def check_if_greater_than_2(num):
    if int(num) > 2:
        return True
    else:
        return False

def find_divisors(num):
    divList = []
    for x in range(2, num):
        if(num % x == 0):
            divList.append(x)
    return divList

user_num = get_user_num()

print(find_divisors(user_num))
