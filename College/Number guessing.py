class Error(Exception):
    pass

class NumberTooLargeError(Error):
    '''Raised when number guessed is too large'''
    pass
class NumberTooSmallError(Error):
    '''Raised when number is too small'''
    pass

n=10


while True:
    num=int(input("Enter your guess:"))
    try:
        if n>num:
            raise NumberTooSmallError
        elif n<num:
            raise NumberTooLargeError
        else:
            break
    except NumberTooLargeError:
        print("The number you guessed is too large")

    except NumberTooSmallError:
        print("The number you guessed is too small")
            
print("Congratulations!, you guessed the right answer!")