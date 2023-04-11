import random

class Error(Exception):
    pass

class NumberTooLargeError(Error):
    '''Raised when number guessed is too large'''
    pass
class NumberTooSmallError(Error):
    '''Raised when number is too small'''
    pass

n=random.randint(1,20)
i=0
print("You have to guess number in the range 1 to 20.")
flag=1
while True:
    num=int(input("Enter your guess:"))
    i+=1
    try:
        if i<3:
            if n>num:
                raise NumberTooSmallError
            elif n<num:
                raise NumberTooLargeError
            else:
                break
        else:
             flag=0
             break
    except NumberTooLargeError:
            print("The number you guessed is too large")

    except NumberTooSmallError:
            print("The number you guessed is too small")
 
if flag==1:
    print("Congratulations!, you guessed the right answer!")
    print("You took ",i," attempts.")
else:
     print("You lost the game :(")