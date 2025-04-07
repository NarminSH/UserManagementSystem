from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserCreateResponse(BaseModel):
    message: str
    user_id: int


class UserProfileResponse(BaseModel):
    user_id: int
    username: str
    email: str
   

    class Config:
        orm_mode = True  