from fastapi import FastAPI
from pydantic import BaseModel

import Generator
from typing import Union

app = FastAPI()

class Password(BaseModel):
    password: str
    strength: str

@app.get("/strong")
def strong_password():
    return Password(password = Generator.generate_password_strong(), strength = "Strong")

@app.get("/medium")
def medium_password():
    return Password(password = Generator.generate_password_medium(), strength = "Medium")
@app.get("/weak")
def weak_password():
    return Password(password = Generator.generate_password_weak(), strength = "Weak")