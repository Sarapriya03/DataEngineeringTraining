class Employee:

    def work(self):
        print("Employee is working")

class Developer(Employee):

    def code(self):
        print("Writing Python code")

class Tester(Employee):

    def test(self):
        print("Testing application")

d1 = Developer()
d1.work()
d1.code()

t1 = Tester()
t1.work()
t1.test()