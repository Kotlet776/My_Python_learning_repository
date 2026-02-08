#4.1 if

i = 3
if i == 2:
    print(f"{i} is eaqual to two")
elif i == 3:
    print(f"{i} is eaqual to three") # this will be printed
else:
    print(f"{i} is neither equal to two or three")

#4.2 for

l = ["apple", "banana", "carrot", "mango"]
for i in l:
    print(i) # the items in the list will be printed in sequence from first to last in different rows

#4.3 range()

for x in range(2, 15, 2):
    print(x) # numbers from two to fourtheen will be printed, but with jumps of 2, so: 2, 4, 6, ..., 14

#4.4 break, continue

for i in range(1, 10):
    if i == 5:
        break # when "i" is eaqual to five this line will run and turn off the whole loop even thoug the range hasn't finished.
    elif i % 2 == 0:
        print(f"{i} is an even number") # this will be printed as long as the loop runs and when the remainder of "i" divided by two is eaqual to zero
        continue # when this runs the loop wil start the next iteratin without executing the rows under the continue (the line 27 will not be printed)
    print(f"{i} is not an equal number") 

#4.6 pass

for item in l:
    pass # is used as a place holder so you can continue on your code without having a syntax error

#4.7 match

a = (3, 2)
match a:
    case (0, 0) | (3,2):
        print("Cool point")
    case (x, y):
        print(x, y)
    case _:
        print("a is not a point") # will be printed if none of the above cases are satisfied

#4.8 Defining functions

def my_function(): # to define a function use the def keyword then name it and add parameters you want to accept
    return "Hi!" # to get back a value, the return keyword has to be used
print(my_function()) # this is how you call a function
f = my_function() # you can save a function call as a variable
print(f) # later you can use the variable to call the function

#4.9.1 Default Arument Values

def my_function2(arg1=5, arg2="arg2"): # you can add default values, those will be used if you don't provide other values in the function call statement
    return(arg1, arg2)
(my_function2())

#4.9.2 Keyword Arguments

def my_function3(arg1="xD"):
    return arg1
print(my_function3(arg1="XD")) # you can add an argument using the keyword for the parameter

#4.9.3 Special parameters

def my_function4(pos_arg1, pos_arg2, /, arg3, *, keywd_arg4, keywd_arg5):
    return "The first two arguments MUST be a position argument. Arg3 can be either, but arg3 and 5 MUST be keyword arguments."

#4.9.4 Arbitrary Argument Lists

def my_function5(*the_list, special_keyword_arg = " "): # saves all values in the first arg and optionaly you can save a value to the keyword arg
    pass

#4.9.5 Unpacking Argument Lists

small_list = [0, 10]
o = list(range(*small_list))
print(o)

#4.9.6 Lambda Expressions

def my_function6(y):
    return lambda x: x * y # lambda is an anonymus one line function that can be nested inside other functinos to save space and make the code more readable
g = my_function6(10)
print(g(5))

#4.9.7 Documentation Strings

def my_function7():
    """
    Docstring for my_function7
    This is a docstring where information about the function should be present
    """
print(my_function7.__doc__)

#4.9.8 Function Annotations

def my_function8(arg1, arg2, arg3) -> int:
    return my_function8.__annotations__

print(my_function8(1, 5, 3))
