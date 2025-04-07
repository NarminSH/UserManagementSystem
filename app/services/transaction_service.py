from sqlalchemy.orm import Session
from domain.schemas.transaction import TransactionCreate
from domain.models.transaction import Transaction


def create_transaction(user_id: int, transaction_data: TransactionCreate, db: Session) -> int:
    new_transaction = Transaction(
        user_id=user_id,
        recipient_id=transaction_data.recipient_id,
        amount=transaction_data.amount,
        currency=transaction_data.currency,
        transaction_type=transaction_data.transaction_type
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction.id
