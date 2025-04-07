from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.services import user_service
from core.security import create_access_token, get_current_user_id
from domain.schemas.token import TokenResponse
from domain.schemas.user import UserCreate, UserCreateResponse, UserProfileResponse
from core.database import get_db


router = APIRouter()

@router.post("/register", response_model=UserCreateResponse)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    print(user_data.email)
    user_result = user_service.create_user(user_data, db)
    return UserCreateResponse(message="User registered successfully", user_id=user_result)


@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_service.authenticate_user(db, form_data.username, form_data.password)
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/profile", response_model=UserProfileResponse)
def get_user_profile(db: Session = Depends(get_db), user_id: str = Depends(get_current_user_id)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserProfileResponse(
        user_id=user.id,
        username=user.username,
        email=user.email
    )