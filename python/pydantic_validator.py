from pydantic import BaseModel, ValidationInfo, field_validator

class User(BaseModel):
    name: str
    password: str

    @field_validator("name")
    @classmethod
    def clean_username(cls, name: str):
        return name.strip().lower()

    @field_validator("password")
    @classmethod
    def check_password(cls, password: str, info: ValidationInfo) -> str:
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        elif info.data["name"] == password.lower():
            raise ValueError("Password cannot be the same as the username")     
        else:
            return password      

user = User(name="     HARSH PARDHI      ",password="harsh@321")
print(user.name)
print(user.password)