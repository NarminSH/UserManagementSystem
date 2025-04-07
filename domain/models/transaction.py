from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from domain.models.base import BaseEntity
from domain.enums.transaction import TransactionType
from domain.enums.currency import Currency

class Transaction(BaseEntity):
    __tablename__ = "transactions"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    recipient_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    amount = Column(Numeric(10,2), nullable=False)
    currency = Column(Enum(Currency), nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    user = relationship("User", back_populates="transactions", foreign_keys=[user_id])
    recipient = relationship("User", back_populates="received_transactions", foreign_keys=[recipient_id])
