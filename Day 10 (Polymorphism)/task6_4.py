# Task 6 - Question 3

class Employee:
    def setEmployee(self, empid, empname):
        self.empid = empid
        self.empname = empname

    def getEmployee(self):
        print("Employee ID =", self.empid)
        print("Employee name =",self.empname)

class Payroll(Employee):
    def setPayroll(self, bs, hra, da):
        self.bs = bs
        self.hra = hra
        self.da = da

    def getPayroll(self):
        print("BS =", self.bs)
        print("HRA =", self.hra)
        print("DA =", self.da)

class Loan:
    def setLoan(self,amt):
        self.amt = amt

class Payslip(Payroll, Loan):
    def netSalary(self):
        print("Net Salary =", (self.bs + self.hra + self.da - self.amt) )

aman = Payslip()
aman.setEmployee(1001, "Aman Chaursiya")
aman.getEmployee()

aman.setPayroll(50000, 15000, 5000)
aman.getPayroll()

aman.setLoan(5000)

aman.netSalary()