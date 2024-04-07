class SoftwareEngineer:
    def __init__(self, name, age):
        # public attribute
        self.name = name
        self.age = age
        # private attribute with access from outside
        self._salary1 = None
        # private attribute with no access from outside
        self.__salary = None
        self.__num_bugs_solved = 0

    # getter
    def get_salary(self):
        return (self.__salary)

    # setter
    def set_salary(self, base_value):
        # check value, enforce constraints
        self.__salary = self._calculate_salary(base_value)
        return self.__salary

    def code(self):
        self.__num_bugs_solved += 1

    def _calculate_salary(self, base_value):
        if self.__num_bugs_solved < 10:
            return base_value
        if self.__num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3


# instance of softwareengineer class
se = SoftwareEngineer("Max", 35)

print(se.name, se.age, se._salary1)  # Max 35 None

# Error :  'SoftwareEngineer' object has no attribute '__salary'
try:
    print(se.__salary)
except Exception as e:
    print("Error : ", e)

print(se.get_salary())  # None
print(se.set_salary(500))  # 1000
print(se.set_salary(25000))  # 20000

for i in range(0, 20):
    se.code()

print(se.set_salary(6000))  # 12000