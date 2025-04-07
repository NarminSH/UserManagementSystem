import re
from fastapi import HTTPException, status

PASSWORD_REGEX = r"^(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,20}$"

def validate_password(password: str):
    if not re.match(PASSWORD_REGEX, password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be between 8 and 20 characters long, contain at least one uppercase letter, one digit, and one special character."
        )