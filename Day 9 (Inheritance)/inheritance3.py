# Multiple Inheritance 

class A:
    def m1(self):
        print("m1 from A class")

class B:
    def m2(self):
        print("M2 from B class")

class C(A,B):
    def m3(self):
        print("M3 from C class")

obj_c = C()
obj_c.m1()
obj_c.m2()
obj_c.m3()