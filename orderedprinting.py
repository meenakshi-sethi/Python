"""
Problem Statement: Ordered Number Printing Using 3 Threads

You are asked to implement a multithreaded solution where three threads work together to print numbers from 1 to 50, in increasing order, one number at a time.

🎯 Requirements:
	•	Print numbers from 1 to 50, inclusive.
	•	Use three threads to perform the printing.
	•	The output on the console must be in sequential order: 1 2 3 4 ... 50
	•	The numbers must not be printed out of order or skipped.
"""

"""
Approach: 
- need to coordinate three threads such that only one prints at a time.
- numbers are printed in order or in sequence
- There will be a shared variable to track the current number to print. 
- Lock is used to ensure that only one thread can print at a time (one thread to access a block of code or data at a time). It doens't necessarily see the order of execution.
  Lock alone ensures mutual exclusion but not the order of in which threads gets to print. So if we only use locks thread execution order is not guaranteed. We will need more logic.
- Condition lets threads wait until some condition becomes true and allows waking up other threads. So condition alone is not enough to solve this because Condition must be used with a Lock 
  (either explicitly or implicitly). It requires a lock to work correctly.
- what Condition does:
	•	It allows threads to wait until they are notified.
	•	It uses the associated lock to: Ensure mutual exclusion while checking conditions or modifying shared variables.
        Block/unblock threads in a coordinated way using wait() and notify()
"""

# importing threadng module
import threading

counter = 1 # global variable (defined outside function) and also shared varaiable that all threads will access and modify.

max_num = 50 # maximun number to print

condition = threading.Condition() # creating a condition object to manage sync between threads. internally includes a lock.

# Function to print numbers in order
num_threads = 3 # number of threads to use

def ordered_print(thread_id):
    global counter # uisng the global variable counter
    while True: # loop to check condition
        with condition: # keeping the critical section where
                while counter <= max_num and (counter % num_threads != thread_id % num_threads): # this ensures round robin execution Thread 3 prints when counter % 3 == 0, Thread 1 prints when counter % 3 == 1 and thread 2 prints when counter % 3 == 2
                    condition.wait() # if above condition fails (false) then wait until notified by another thread
                if counter > max_num:
                    condition.notify_all() # notify all threads to wake up and check the condition again
                    break # exit the loop if counter exceeds max_num

                print(f"Thread {thread_id} prints --> {counter}") # print the current number
                counter += 1 # increment the counter

                condition.notify_all() # notify all threads that counter has been changed and recheck their turn

# Creating threads
t1 = threading.Thread(target=ordered_print, args=(1,)) # thread 1
t2 = threading.Thread(target=ordered_print, args=(2,)) # thread 2
t3 = threading.Thread(target=ordered_print, args=(3,)) # thread 3

# Starting threads
t1.start()
t2.start()
t3.start()  


# waiting for threads to complete
t1.join()
t2.join()
t3.join()   

print("Done with ordered printing using 3 threads")


