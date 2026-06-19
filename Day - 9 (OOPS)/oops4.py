class Student:
    university = "AKTU"
    def __init__(self, name, dob, branch):
        self.name = name
        self.dob = dob
        self.branch = branch
    
    def display_data(self):
        print("University =", self.university)
        print("Name =", self.name)
        print("DOB =", self.dob)
        print("Branch =", self.branch)

asif = Student("Mohammad Asif", "17/10/1970", "CSE")
asif.display_data()