from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./multineiro.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    active_modules = Column(String)  # JSON list, e.g. '["jurist","auto"]'
    created_at = Column(DateTime, default=datetime.utcnow)
    chats = relationship("Chat", back_populates="user")

class Promokod(Base):
    __tablename__ = "promokods"
    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    modules = Column(String)  # JSON '["jurist","auto"]'
    used = Column(Boolean, default=False)

class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    module_id = Column(String)
    messages = Column(Text)  # JSON list of {"role": "user|ai", "content": "..."}
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="chats")

Base.metadata.create_all(bind=engine)
