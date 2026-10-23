from pydantic import BaseModel,Field

class User(BaseModel):
    id: int=Field(default=101,ge=100,le=200,description="The ID of the user")
    name: str=Field(default="John Doe",min_length=3,max_length=50,description="The name of the user")

data = {"id": 202, "name": "Harsh Pardhi"} 
user = User(**data)
print(user)     