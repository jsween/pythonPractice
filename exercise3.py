def cut_off_high(numList, maxNum, emptyList):
    for x in numList:
        if(x < maxNum):
            emptyList.append(x)
    return emptyList

def check_if_num(string):
    isInteger = False
    while not isInteger:
        num = input(string)
        isInteger = represents_int(num)
        if(isInteger):
            return int(num)
        else:
            print("Really?  Just enter a valid number.\n")

def represents_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def get_user_num():
    string = "Please enter a number: "
    return check_if_num(string)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
message = "Enter a max number: "
maxNum = get_user_num()
print(cut_off_high(a, maxNum, b))
