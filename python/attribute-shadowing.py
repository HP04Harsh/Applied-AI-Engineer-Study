class Rect:
    size = 40

    def display(self):
        print(f"Size: {self.size}")

obj = Rect()
obj.size = 100
del obj.size  # This will delete the instance attribute 'size', reverting to the class attribute
obj.display()  # Output: Size: 40      