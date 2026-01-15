class Person:
    def __init__(self, name):
        self._name = name 

    def info(self):
        return "Person name: " + self._name


class Student(Person): 
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def info(self):  
        return "Student name: " + self._name + ", ID: " + str(self.student_id)


p = Person("Arai")
s = Student("Lym", 101)

print(p.info())
print(s.info())
