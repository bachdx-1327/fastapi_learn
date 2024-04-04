from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from typing import Optional

class Text(BaseModel):
    text_id: int
    text: str
    text_summaries: Optional[str]

class textCreate(BaseModel): 
    text_summaries: Optional[str]
