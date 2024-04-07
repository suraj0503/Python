
class SoftwareEngineer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__salary=None

    @property
    def salary(self):
        return(self.__salary)

    @salary.setter
    def salary(self,value):
        self.__salary = value

    @salary.deleter
    def salary(self):
        del self.__salary

se = SoftwareEngineer("mark",45)

se.salary=6000
print(se.salary) #6000
del se.salary

#Error :  'SoftwareEngineer' object has no attribute '_SoftwareEngineer__salary'
try:
    print(se.salary)
except Exception as e:
    print("Error : ",e)