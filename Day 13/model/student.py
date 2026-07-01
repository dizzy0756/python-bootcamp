class Student:
    def __init__(self,id, name, course, age):
        self.id = id
        self.name = name
        self.course = course
        self.age = age

    def to_dict(self):
        return{
            "id" :  self.id,
            "name" : self.name,
            "course" : self.course,
            "age" : self.age
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(id = data["id"], name = data["name"], course = data["course"], age = data["age"])
    
    def to_tuple(self):
        return (self.id,self.name,self.course,self.age,)