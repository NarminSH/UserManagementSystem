import enum


class TransactionType(str, enum.Enum):
    deposit = "deposit"
    withdrawal = "withdrawal"
    transfer = "transfer"