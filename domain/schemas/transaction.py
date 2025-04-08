from typing import Optional
from pydantic import BaseModel, root_validator
from domain.enums import TransactionType, Currency
from decimal import Decimal


class TransactionCreate(BaseModel):
    amount: Decimal
    currency: Currency
    transaction_type: TransactionType
    recipient_id: Optional[int]= None
    
    @root_validator(pre=True)
    def normalize_recipient_id(cls, values):
        if values.get("recipient_id") == 0:
            values["recipient_id"] = None
        return values
    
    @root_validator(skip_on_failure=True)
    def check_transfer_has_recipient(cls, values):
        if values.get("transaction_type") == TransactionType.transfer and not values.get("recipient_id"):
            raise ValueError("recipient_id is required for transfer transactions")
        return values


class TransactionCreateResponse(BaseModel):
    transaction_id: int
    status: str



