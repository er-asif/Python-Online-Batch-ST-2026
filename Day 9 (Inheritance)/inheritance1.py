class Parent:
    def sayhello(self):
        print("Hello")

class Child(Parent):
    def say_goodbye(self):
        print("Good byee.....")

ch = Child()
ch.sayhello()
ch.say_goodbye()
