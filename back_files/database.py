from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///database.db", echo=True)  
def init_db():
    from models import Post
    SQLModel.metadata.create_all(engine)