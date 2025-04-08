from sqlalchemy.orm import Session
from domain.enums.transaction import TransactionType
from domain.models.user import User
from domain.schemas.transaction import TransactionCreate
from domain.models.transaction import Transaction
from fastapi import HTTPException


def create_transaction(user_id: int, transaction_data: TransactionCreate, db: Session) -> int:
    if user_id is not None:
        sender: User = db.query(User).filter(User.id == user_id).first()
        
    if not sender:
        raise HTTPException(status_code=404, detail="Sender not found")
    
    if sender.balance < transaction_data.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    recipient = None
    if transaction_data.recipient_id:
        recipient = db.query(User).filter(User.id == transaction_data.recipient_id).first()
        if not recipient:
            raise HTTPException(status_code=404, detail="Recipient not found")
        
    
    new_transaction = Transaction(
        user_id=sender.id,
        recipient_id=recipient.id if recipient else None,
        amount=transaction_data.amount,
        currency=transaction_data.currency,
        transaction_type=transaction_data.transaction_type
    )
    db.add(new_transaction)
    
    if transaction_data.transaction_type == TransactionType.deposit:
        sender.balance += transaction_data.amount

    elif transaction_data.transaction_type == TransactionType.withdrawal:
        sender.balance -= transaction_data.amount

    elif transaction_data.transaction_type == TransactionType.transfer:
        sender.balance -= transaction_data.amount
        recipient.balance += transaction_data.amount

    db.add(sender)
    if recipient:
        db.add(recipient)

    db.commit()
    db.refresh(new_transaction)
    
    return new_transaction.id

