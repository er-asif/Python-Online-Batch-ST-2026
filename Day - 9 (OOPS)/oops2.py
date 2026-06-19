class Student:
    university = "Integral University"
    def submit_fee(self, amt):
        print(f"{amt} is Submitted")
    def show_profile(self):
        print("Profile Data  ---------  ")
    

std1 = Student()
print(std1.university)
std1.submit_fee(15000)
std1.show_profile()
