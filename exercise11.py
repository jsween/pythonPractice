isGameOver = False

def exit_game():
    a = input("Press 'x' to exit game or any key to continue: ")
    if(a == 'x'):
        return True

def check_if_prime(num):
    if(num == 1):
        return False
    elif(num == 2):
        return True
    else:
        for x in range(2, num - 1):
            if num % x == 0:
                return False
        return True

def display_result(a):
    if (a):
        print(str(num) + " IS A PRIME NUMBER!!!!")
    else:
        print(str(num) + " is not a prime number")

while(not isGameOver):
    num = int(input("Enter a number: "))
    isPrime = check_if_prime(num)
    display_result(isPrime)
    isGameOver = exit_game()
