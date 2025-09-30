class Student:

    college_name= "IITj"

    def __init__(self, first_name, last_name,age, subject):
        self.first_name= first_name
        self.last_name= last_name
        self.__age=age
        self.subject= subject

    def full_name(self):
        return f"{self.first_name}, {self.last_name}"

    def student_age(self):
        return f"The student name is {self.first_name} and age is {self.__age}" 
    
     # Getter method for __age
    @property   #It turns a method into an attribute.
    def age(self):
        return self.__age

student1= Student("RAM", "Maurya", "23", "sanskrit")
student2= Student("Upender", "Maurya", "24", "geology")

print(student1.full_name())

#print(student1.__age())
print(student1._Student__age)

print(student1.age)
