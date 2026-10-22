class A:
    def sleepA(self):
        return "Sleeping in A"  #Base class 

class B(A):
    def sleep(self):
        return super().sleepA()  # Call the base class method        

obj = B()
print(obj.sleep())  # Output: Sleeping in B
print(B.__mro__)  # Output: (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


