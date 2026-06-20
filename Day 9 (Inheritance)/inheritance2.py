# Multi Level Inheritance

class A:
    def m1(self):
        print("M1 from A class")

class B(A):
    def m2(self):
        print("M2 from B class")

class C(B):
    def m3(self):
        print("M3 from C classs")

obj_c = C()
obj_c.m1()
obj_c.m2()
obj_c.m3()

