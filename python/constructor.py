class A:

    def __init__(self,name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}, World!"

obj = A("Harsh")
print(obj.greet())  # Output: Hello Harsh, World!            