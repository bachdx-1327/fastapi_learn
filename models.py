from sqlalchemy import Column, Integer, String, ForeignKey, DATE, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Summaries(Base): 
    
    __tablename__ = "Summary Table"

    text_id = Column(Integer, primary_key=True, index=True)
    text = Column(String) 
    text_sum = Column(String) 