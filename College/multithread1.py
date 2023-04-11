import threading
from threading import *

print(current_thread().getName())
def mt():
    print("Executing thread: ",current_thread().getName())

child=Thread(target=mt)
child.start()

print("Executing thread ",current_thread().getName())