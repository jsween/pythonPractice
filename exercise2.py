def check_if_num(string):
    isInteger = False
    while not isInteger:
        num = input(string)
        isInteger = represents_int(num)
        if(isInteger):
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
    string = "Please enter a number: "
    return check_if_num(string)

def get_user_check():
    string = "Give me a 2nd number: "
    return check_if_num(string)

def is_even_or_odd(num1, num2):
    numArray = [num1, num2]
    for x in numArray:
        get_num_status(x)

def get_num_status(num):
    if(num % 2 == 0):
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")

def is_num1_divisible_num2(num1, num2):
    if(num2 == 0):
        print(str(num1) + " divided by 0 is undefined")
    elif(num1 % num2 == 0):
        print(str(num1) + " is divisible by " + str(num2))
    else:
        print(str(num1) + " is not divisible by " + str(num2))

num = get_user_num()
check = get_user_check()

is_even_or_odd(num, check)
is_num1_divisible_num2(num, check)
