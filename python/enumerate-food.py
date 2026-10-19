fruits = ["apple", "banana", "orange", "grape"]
prices = [20, 30, 15, 25]

for fruits,prices in zip(fruits, prices):
    print(f"The price of {fruits} is {prices} dollars.")