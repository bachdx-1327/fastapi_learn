from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String 
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///summeries.db', echo=True)
Base = declarative_base()

class Summaries(Base): 
    
    __tablename__ = "Summary Table"

    text_id = Column(Integer, primary_key=True, index=True)
    text = Column(String) 
    text_sum = Column(String) 

    def __init__(self, text, text_sum): 

        self.text = text 
        self.text_sum = text_sum 

Base.metadata.create_all(engine)
