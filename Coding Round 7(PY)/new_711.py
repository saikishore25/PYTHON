# Threading, We have two modules 
# 1. thread - One of the old module which is deprecated but still in use to handle backwards computer systems 

import _thread
import time 

def test(name, delay):
    i = 1 

    while(i<=2):

        time.sleep(delay)
        print("Running First Thread: ", name)
        i = i + 1 

_thread.start_new_thread(test,('first thread', 2))
_thread.start_new_thread(test,('second thread', 3))

