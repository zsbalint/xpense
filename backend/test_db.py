from app.db.session import engine
from app.db.base import Base
from app.db.models import *

# Create all tables defined in models (currently none)
Base.metadata.create_all(bind=engine)

print("Database connection successful!")
