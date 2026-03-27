from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel
import os

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./movies.db")
connect_args = {"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director = Column(String)
    year = Column(Integer)

Base.metadata.create_all(bind=engine)

class MovieBase(BaseModel):
    title: str
    director: str
    year: int

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int
    class Config:
        from_attributes = True

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/movies", response_model=MovieResponse)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    db_movie = Movie(title=movie.title, director=movie.director, year=movie.year)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@app.get("/movies", response_model=list[MovieResponse])
def get_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = db.query(Movie).offset(skip).limit(limit).all()
    return movies

@app.get("/movies/{movie_id}", response_model=MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404)
    return movie