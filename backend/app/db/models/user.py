from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    name: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    # Relationships
    memberships: Mapped[list["GroupMembership"]] = relationship("GroupMembership", back_populates="user")
    expenses: Mapped[list["Expense"]] = relationship("Expense", back_populates="user")
    bank_transactions: Mapped[list["BankTransaction"]] = relationship("BankTransaction", back_populates="user")
    categorization_rules: Mapped[list["CategorizationRule"]] = relationship("CategorizationRule", back_populates="user")

