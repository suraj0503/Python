class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def __str__(self):
        str = f"{self.name} {self.age} is working in OpenAI with salary of {self.salary} doller"
        return str

    def work(self):
        return f"{self.name} is working ..."

class SoftwareEngineer(Employee):
    #extend
    def __init__(self,name,age,salary,level): # overriding the init functionality of parent sclass
        #we can use the init function from its base class using keyword super
        super().__init__(name,age,salary) #calling base initializer
        self.level= level

    def debug(self):
        print(f"{self.name} is debugging ...")

    #functions overloading
    def work(self):
        return f"{self.name} is coding ..."

class Designer(Employee):

    def draw(self):
        print(f"{self.name} is drawing ...")

    #functions overloading
    def work(self):
        return f"{self.name} is designing ..."

se = SoftwareEngineer("david",25,6000,"Junior")
d = Designer("raman",28,7000)

print(se) #david 25 is working in OpenAI with salary of 6000 doller
print(d) #raman 28 is working in OpenAI with salary of 7000 doller

print(se.work()) #david is coding ...
print(d.work()) #raman is designing ...
print(se.level) # this level attribute will only work for software engineer class, not for general employee or the designer

se.debug() #david is debugging ...
d.draw() #raman is drawing ...

#'SoftwareEngineer' object has no attribute 'draw' : error occured
try:
    se.draw()
except Exception as e:
    print(f"{e} : error occured")

