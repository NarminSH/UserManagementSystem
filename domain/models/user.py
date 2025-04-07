from sqlalchemy import Column, String
from domain.models.base import BaseEntity
from sqlalchemy.orm import relationship


class User(BaseEntity):
    __tablename__ = "users"
    
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String, nullable=False) 
    transactions = relationship("Transaction", back_populates="user", foreign_keys="[Transaction.user_id]")
    received_transactions = relationship("Transaction", back_populates="recipient", foreign_keys="[Transaction.recipient_id]")


    