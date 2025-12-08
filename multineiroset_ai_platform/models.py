from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    promokod: str

class UserOut(BaseModel):
    id: int
    email: str
    active_modules: List[str]

class Login(BaseModel):
    email: EmailStr

class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    module_id: str
    message: str
    template: Optional[str] = None

class Module(BaseModel):
    id: str
    name: str
    prompts: List[str]
