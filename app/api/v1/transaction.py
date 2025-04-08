from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from domain.schemas.transaction import TransactionCreate, TransactionCreateResponse
from core.database import get_db
from core.security import get_current_user_id
from app.services import transaction_service

router = APIRouter()


@router.post("/transactions", response_model=TransactionCreateResponse)
def make_transaction(
    transaction_data: TransactionCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)):
    
    tr_id = transaction_service.create_transaction(user_id, transaction_data, db)
    return TransactionCreateResponse(transaction_id=tr_id, status="success")
