class Student:
    university = "AKTU"
    def set_value(self, name, dob, branch):
        self.name = name
        self.dob = dob
        self.branch = branch

    def display_data(self):
        print("University =", self.university)
        print("Name =", self.name)
        print("DOB =", self.dob)
        print("Branch =", self.branch)

name = input("Enter your name ")
dob = input("Enter your DOB ")
branch = input("Enter your branch ")

aman = Student()
aman.set_value(name,dob,branch)
aman.display_data()

# anish = Student()
# anish.set_value("Anish Kumar", "12/10/2000", "Mechanical")
# anish.display_data()