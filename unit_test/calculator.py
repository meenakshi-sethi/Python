# unit testign with function (without class)

def calc_add(num1, num2):
    return num1 + num2


if __name__ == "__main__":
    print("Import and use me!")


"""
When we run this module or code as is direclty (file or script) then peice of code where we have __name__ == "__main__" will get executed or whatever we might have of these if condition and it will print Import and use me!

but when we import this module then `if __name__` peice of code will not get executed but all the functions and methods that is there will become avaiable to us. 
in this case when we import, we will have the function calc_add avaiable to us to use. But when we run the file directly it will only print import and use me text
"""