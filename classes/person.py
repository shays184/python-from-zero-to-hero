
# float, int, list, tuple, dict, set, str, bool
# Object-oriented programming (OOP / OOD) תכנות מונחה עצמים


class Person:
    def __init__(self, name : str = None, birth_year: int = None):
        self.name = name
        self.birth_year = birth_year
        self.age = self.calc_age() #calc_age is a method that returns the age of the SPECIFIC person

    def __str__(self) -> str:
        return f"Name: {self.name}\nAge: {self.age}"

    def calc_age(self) -> int: #method
        return 2025 - self.birth_year
    
    def hi(self):
        print("Hi, I'm", self.name)


class IsraeliPerson(Person):

    def __init__(self, name, birth_year, id_number: str):
        super().__init__(name, birth_year) # super means to call the parent class
        self.id_number = id_number

    def hi(self):
        print("Shalom, ani", self.name)


class SpanishPerson(Person):
    def hi(self):
        print("Hola, soy", self.name)

class CustomList(list):
    def __init__(self, *args):
        super().__init__(*args)

    def count_ints(self):
        count = 0
        for item in self:
            if type(item) == int:
                count += 1
        return count
    



l1 = CustomList([1, 2, 3, "x", "y", 4])
print(l1.count_ints())
l1.append("p")
print(l1)


