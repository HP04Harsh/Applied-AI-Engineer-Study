# Static Method 
# class A:
#     name = "Harsh"
#     @staticmethod
#     def greet():
#         return f"Hello {A.name}, World!"
# print(A.greet())  # Output: Hello Harsh, World!        


# Class Method
class A:

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    
    @classmethod
    def person_name(cls, name):
        name,surname = name.split("-")
        return cls(name,surname)  # Create an instance of the class using the first part of the name

obj = A.person_name("Harsh-Pardhi")
print(obj.name)
print(obj.surname)