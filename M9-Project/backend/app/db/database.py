from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This creates a file named 'pantry.db' in your project folder
SQLALCHEMY_DATABASE_URL = "sqlite:///./pantry.db"

# The engine is what actually talks to the database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# This is a 'Session' which is like a temporary connection to run a command
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# We use this 'Base' to create our data models (tables)
Base = declarative_base()

# Helper function to get a database connection and close it when done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()