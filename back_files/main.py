from fastapi import FastAPI
from sqlmodel import Session, select
from database import engine, init_db
from models import Brainrot

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
     init_db()

@app.get("/brainrots")
def get_brainrots():
    with Session(engine) as session:
        statement = select(Brainrot)
        results = session.exec(statement).all()
        return results

@app.post("/brainrots")
def add_brainrot(brainrot: Brainrot):
    with Session(engine) as session:
        session.add(brainrot)
        session.commit()
        session.refresh(brainrot)
        return brainrot