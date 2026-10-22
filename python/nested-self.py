class Chai:
    size = "150"

    def describe(self):
        return f"This is a {self.size} ml cup of Chai."

ginger_T = Chai()
print(ginger_T.describe())
print(Chai.describe(ginger_T))  # Calling the method using the class name and passing the instance explicitly