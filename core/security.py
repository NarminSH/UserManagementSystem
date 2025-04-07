from datetime import datetime, timedelta
from jose import jwt, JWTError
from core import config
from typing import Union
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from core import config
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=int(config.ACCESS_TOKEN_EXPIRE_MINUTES)))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY)
    return encoded_jwt



def get_current_user_id(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    print(token + " token over here")
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        user_id: str = int(payload.get("sub"))
        print(user_id)
        if user_id is None:
            print("username nonedirrr")
            raise credentials_exception
        return user_id
    except JWTError as e:
        print(repr(e))
        print("yuxxxxxxxarida jwt error")
        raise credentials_exception