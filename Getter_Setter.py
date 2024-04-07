class SoftwareEngineer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__salary=None

    #getter
    def get_salary(self):
        print(self.__salary)
        return(self.__salary)

    #setter
    def set_salary(self,value):
        self.__salary= value
        print(self.__salary)
        return self.__salary

se = SoftwareEngineer("mark",45)

se.get_salary() #None
se.set_salary(5000) #5000
