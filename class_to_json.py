import json

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s = Student("Nurali",15)
print(json.dumps(s.__dict__))
