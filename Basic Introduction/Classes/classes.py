class myClass():
    def method1(self):
        print("Method 1")
    
    def method2(self, string):
        print("Method 2 " + string)
    
# Inheritance
class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("Method 1 Another Class")
    
    def method2(self, string):
        print("Method 2 ")

def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c1 = anotherClass()
    c1.method1()
    c1.method2("This is string from another class")


if __name__ == "__main__":
    main()