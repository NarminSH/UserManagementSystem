from core.database import Base
from sqlalchemy import Column, DateTime, Boolean, Integer
from sqlalchemy.sql import func


class BaseEntity(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now()) 
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  
    is_deleted = Column(Boolean, default=False) 