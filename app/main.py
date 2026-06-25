from app.database.database import engine
from app.database.base import Base

import app.models


Base.metadata.create_all(bind=engine)

print("Database OK")
