from typing import Optional
from pydantic import BaseModel
from domain.enums import TransactionType, Currency
from decimal import Decimal


class TransactionCreate(BaseModel):
    amount: Decimal
    currency: Currency
    transaction_type: TransactionType
    recipient_id: Optional[int]


class TransactionCreateResponse(BaseModel):
    transaction_id: int
    status: str
