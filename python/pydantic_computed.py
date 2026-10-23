from pydantic import BaseModel, Field, computed_field

class Item(BaseModel):
    quantity: int
    price: int

    @computed_field
    @property
    def total(self) -> int:
        return self.quantity * self.price
item = Item(quantity=3, price=5)
print(item.quantity)  # Output: 3
print(item.price)     # Output: 5
print(item.total)     # Output: 15

