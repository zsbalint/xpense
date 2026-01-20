from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String, default="")

    # Self-referencing foreign key
    parent_category_id: Mapped[int | None] = mapped_column(
        ForeignKey("categories.id"),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    # Relationships
    parent: Mapped["Category | None"] = relationship(
        "Category",
        remote_side=[id],
        back_populates="children",
    )

    children: Mapped[list["Category"]] = relationship(
        "Category",
        back_populates="parent",
    )

    expenses: Mapped[list["Expense"]] = relationship(
        "Expense", back_populates="category"
    )

    bank_transactions: Mapped[list["BankTransaction"]] = relationship(
        "BankTransaction", back_populates="category"
    )

    categorization_rules: Mapped[list["CategorizationRule"]] = relationship(
        "CategorizationRule", back_populates="category"
    )
