# Exception Handling or Error Handling
'''
Errors and Exceptions:
Both errors and exceptions represent issues that disrupt the normal flow of a program, but they differ 
slightly in scope and handling.

-----------------------------------------------------------------------------------------------------------
What are Errors? 
Errors are problems in a program that cannot usually be handled. They typically occur 
due to issues in the code itself.

Types of Errors
 
 - Syntax Errors (Compile-time errors): Occur when Python can't interpret code due to incorrect syntax  
    syntax is incorrect. Also known as syntactical error, such as:
        Missing colons (:)
        Wrong spelling of keywords
        Unmatched quotes: `print('Hello")`
        Missing parentheses or brackets
    
        Eg print("Hello" # Output: SyntaxError: unexpected EOF while parsing
    
        These errors are easy to debug since they are caught at compile/parse time and 
        prevent the program from running.
 _________________________________________________________________________________________________________

 - Logical Errors: Code runs without crashing, but produces incorrect output/results
        Code compiles successfully with correct syntax
        Program runs without crashing
        Output is produced but it's incorrect
        Example: Using wrong formula in calculations

    Eg. 
        def add(a,b):
            return a - b # logic error. It should be a + b

    These errors are harder to find and require thorough testing to identify incorrect behavior. 
 
__________________________________________________________________________________________________________    

 - Runtime Error: Errors that occur while the program is running. Here code is correct (no syntax errors)
    and logic is also correct (no logical errors)
        Code compiles successfully (no syntax errors)
        Logic appears correct (no obvious logical errors)
        Error occurs during program execution due to:
        Invalid user input
        File not found
        Network connectivity issues
        Division by zero
        Memory issues

    These are EXCEPTIONS in python. 

_________________________________________________________________________________________________________

## Types of Statements
  - Normal Statements: Statements that typically don't cause errors.
  - Critical Statements: Statements that might cause runtime errors.

---------------------------------------------------------------------------------------------------------
What are Exceptions?
Exceptions are runtime errors that Python can detect and handle gracefully using `try` and `except` blocks.
[try, except, else, finally block]

The main reason for using exception handling is to ensure that program execution does not stop when an error 
occurs.

    Types of Built-in Exceptions
    | Exception           | Description                               |
    | ------------------- | ----------------------------------------- |
    | `ZeroDivisionError` | Division by zero                          |
    | `FileNotFoundError` | File not found                            |
    | `ValueError`        | Invalid value for a function or operation |
    | `IndexError`        | Index out of range in lists or strings    |
    | `KeyError`          | Missing key in a dictionary               |
    | `TypeError`         | Inappropriate type used                   |
    | `AttributeError`    | Accessing a non-existent attribute        |
    | `ImportError`       | Import failed                             |
    | `NameError`         | Using an undefined variable               |
    |_____________________|___________________________________________|

___________________________________________________________________________________________________________
    
Python Exception Hierarchy

BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    │   └── UnicodeError
    ├── TypeError
    ├── FileNotFoundError
    └── RuntimeError
    
-----------------------------------------------------------------------------------------------------
Error Handling vs Exception Handling

| Aspect              | Error Handling                               | Exception Handling                        |
| ------------------- | -------------------------------------------- | ----------------------------------------- |
| Scope               | Deals with **syntax or logical errors**      | Deals with **runtime exceptions**         |
| Detectable by code? | Not usually (syntax/logic errors break flow) | Yes, can be caught using `try-except`     |
| Recoverable?        | No (syntax/logic errors must be fixed)       | Yes, exceptions can be caught and handled |
| Tool used           | Linter, debugger, unit tests                 | `try`, `except`, `finally`, `raise`       |

'''
## Basic Exception Handling

### Problem Without Exception Handling
a = 5
b = 0
print(a/b)  # ZeroDivisionError: division by zero
print("bye")  # This line won't execute - program stops


### Solution With Try-Except
a = 5
b = 0
try:
    print(a/b)  # critical statement
except Exception as e:
    print("Cannot divide by Zero. Error:", e)
print("Bye")  # This will always execute


## Complete Try-Except-Else-Finally Structure

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input. Enter a number.")
#else:
#    print("Optional")
finally:
    print("Execution completed.")


### Else Block (Optional): Executes only if no exception occurs in try block:
### Finally Block (Optional) Always executes, regardless of whether an exception occurred:
#finally:# Cleanup code (close files, database connections, etc.)
#    print("Cleanup completed")

'''
## Best Practice: Use Separate try-except Blocks for Independent Operations
    Although Python allows multiple error-prone statements in one try block with multiple excepts, it's not 
    recommended when the operations are independent.
        - If one error occurs, the rest of the code in the try block is skipped.
        - This means only the first exception is handled and others are never reached.

    Best Practice: Use separate try-except blocks for each risky operation.
    Benefits:
    - Ensures all errors are checked and handled.
    - Improves readability, debugging and execution flow.
    - Prevents one failure from blocking the rest.
        
Tip: One try = one risky task = one clear exception to handle.

'''
# Not Recommended: One try Block for Multiple Errors
try:
    result = 10 / 0 # ZeroDivisionError
    print([1, 2, 3][5]) # Skipped
    print({"name": "Alice"}["age"]) # Skipped
except ZeroDivisionError:
    print("Caught ZeroDivisionError")
except IndexError:
    print("Caught IndexError")
except KeyError:
    print("Caught KeyError")

## After the first error (10 / 0), the rest of the try block is skipped other errors are never reached.

# Recommended: Separate try-except Blocks
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError")

try:
    print([1, 2, 3][5])
except IndexError:
    print("Caught IndexError")

try:
    print({"name": "Alice"}["age"])
except KeyError:
    print("Caught KeyError")

## All errors are tested and handled independently
