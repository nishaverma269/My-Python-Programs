#Define basic function
def func1():
    print("This is a function");

#Function with arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

#Function returns a value
def func3(x):
    return x*x*x

#Function with default value
def func4(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#Function with variable number of arguments
def func5(*args):
    result = 0
    for x in args:
        result = result + x
    return result

#Call functions
func1()
print(func1()) #This will print values along with none because function has no return value
print(func1) #This will return only the value of func1 since () has not been used.

func2(10, 20)
print(func2(10,20))

print(func3(3))

print(func4(2))
print(func4(2,3))
print(func4(x=3, num=2)) #No particular order of passing arguments

print(func5(10, 4, 5, 10, 4))