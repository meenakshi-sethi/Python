# Multi-Threading

'''
Multithreading means running multiple threads (smaller units of a process) concurrently within a 
single process. It's useful for I/O-bound tasks like file operations, API calls or web scraping.

Python uses the `threading` module for multithreading

Key Points:
  - Threads share the same memory space.
  - Python has a Global Interpreter Lock (GIL) which allows only one thread to execute Python bytecode 
    at a time hence CPU-bound tasks dont benefit much.
  - Good for tasks like: downloading files, reading/writing to disk, making API calls.
  - Python switches between threads while waiting (non-blocking).

    [ Main Program ]
       |
   --------------------
   |        |         |
Thread 1  Thread 2  Thread 3
   |        |         |
 Read    API Call   Write File
  

# Global Interpreter Lock (GIL)
Python's threading capabilities are unique due to the Global Interpreter Lock (GIL), which affects how 
true parallelism works compared to other languages.

The GIL is a mutex (lock) that allows only one thread to execute Python bytecode at a time, even on 
multi-core systems.

Python (specifically CPython) has a Global Interpreter Lock (GIL), which means only one thread executes 
Python bytecode at a time, even if you have multiple threads. 

This prevents true parallelism on multi-core systems, so multithreading doesnot improve performance 
for CPU-bound tasks.


=========================================================================================================
CPU-bound tasks: These are tasks that spend most of their time doing computations, like heavy mathematical 
calculations, data processing, or image manipulation. Since these tasks are constantly executing Python 
bytecode, they are blocked by the GIL. Spawning multiple threads for a CPU-bound task on a multi-core 
system will not make it run faster. In fact, the overhead of context switching between threads can even 
slow it down.

I/O-bound tasks: These are tasks that spend most of their time waiting for input/output operations, such 
as reading/writing files, making network requests, or interacting with a database. In these cases, the GIL 
is released during the waiting period, allowing another thread to acquire the GIL and run. This is why 
multithreading is still a valuable tool for I/O-bound tasks in Python, as it allows for concurrency and 
prevents program from being idle while waiting for I/O.
==========================================================================================================



'''
# STEP 1: Basic example without threads (sequential execution)

class Hello():
    def run(self):
        for i in range(5):
            print("Hello")

class Hi():
    def run(self):
        for i in range(5):
            print("Hi")

# sequential execution
t1 = Hello()
t2 = Hi()

t1.run()
t2.run()

"""
# Output
Hello
Hello
Hello
Hello
Hello
Hi
Hi
Hi
Hi
Hi
"""

# STEP 2: Using Threads for concurrent execution

"""
To run Hello and Hi concurrently, we use threading.Thread. Instead of calling `run()` directly, we 
call `start()` which triggers the thread and calls `run()` internally.
"""

from threading import Thread

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello..")

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi..")

t1 = Hello()
t2 = Hi()

t1.start()
t2.start()

"""
Expected Output:
Hello
Hi
Hello
Hi
...

Actual Output
Hello..
Hello..
Hello..
Hello..
Hello..
Hi..
Hi..
Hi..
Hi..
Hi..
"""

# STEP 3: Introducing delay using sleep()
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello****")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi****")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)  # delay helps reduce console clutter
t2.start()

"""
This will print messages with a 1-second delay between each and a slight wait between Hello and Hi.

Expected output
Hello****
Hi****
Hello****
Hi****
----
Same actual output
"""

# STEP 4: Using join() to wait for threads to finish
"""
By default, the main thread continues to execute while child threads are running.
If we want the main thread to wait until both threads finish, use .join().
"""
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello****")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi****")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2) 
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Bye")  # Will only print once both threads are done





# thread_custom_method
# NOTE: Only `run()` works with `start()` in threading?
"""
When we create a thread using the `Thread` class and call `start()`, Python **only looks for the `run()` 
method** to execute in the new thread.

If you define we own custom method (like `say_hello()`), it wont be executed by default.

To run your custom method in a thread, we must call it **inside the `run()` method**.

See example below

"""
from threading import Thread

class MyThread(Thread):
    def say_hello(self):
        print("Hello from my custom method!")

    def run(self):
        self.say_hello()  # Calling custom method inside run()

t = MyThread()
t.start()
t.join()

"""
Key Point:
- `start()` --> runs `run()` method internally
- To run any other method (eg `say_hello()`), call it from inside `run()`
"""


# Creating thread without using class or overriding run method
'''
Alternative way to create thread without using class or overriding run method.

We can pass a normal function directly using `target=` while creating the thread.

start() will then run that function in a separate thread.

This is useful when we just want to run simple functions concurrently and dont want to create classes.

Lets take 2 simple functions and run them in parallel using threading.Thread.
'''

from threading import Thread
from time import sleep

def greet_hello():
    for i in range(5):
        print("Hello")
        sleep(1)

def greet_hi():
    for i in range(5):
        print("Hi")
        sleep(1)

# creating threads by passing functions using target
t1 = Thread(target=greet_hello)
t2 = Thread(target=greet_hi)

# starting both threads
t1.start()
t2.start()

# wait for both threads to complete
t1.join()
t2.join()

print("Main program done")

'''
Expected Output (order may vary):
Hello
Hi
Hello
Hi
...
Main program done

So here we are not using any class or run method. We just passed functions to the Thread constructor using target.
Thread will run those functions concurrently in two separate threads.
'''
