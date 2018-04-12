# Declare a variable
i = 0
print(i)

#Re-declaring the variable
i="abc"
print(i)

#You cannot combine two datatypes in Python. Either one has to convert and match the other.
print("this is a string  " + str(123))

#Global vs. local variables 
j = 0
def printFunction():
    global j
    j = "def"
    print(j)

printFunction()
print(j)

del j #deletes the variable j
print(j)