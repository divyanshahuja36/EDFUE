from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    grade_class: str
    contact: str
    expectations: str = ""
    password: str
