# Different Built in Methods present in Python Multithreading 
# 1. current_thread()
# IT RETURNS THE CURRENT THREAD OBJECT 

import threading 

print(threading.current_thread())       # It returns the Current Thread Object which shows its name and TID (Thread ID)
print(threading.current_thread().name)   # Name attribute returns only the name of thread
print(threading.current_thread().ident)  # ident attribute returns only the ID of thread 
print(threading.current_thread().is_alive)  # Checks whether the thread is alive or not returns a boolean value 





