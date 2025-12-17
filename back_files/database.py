from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///database.db", echo=True)  
def init_db():
    from models import Brainrot
    SQLModel.metadata.create_all(engine)