from pydantic import BaseModel


class TokenResponse(BaseModel):
    access_token: str
    token_type: str

# class TokenData(BaseModel):
#     email: str | None = None
