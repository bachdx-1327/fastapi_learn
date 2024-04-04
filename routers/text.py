from fastapi import Request

from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from database import get_db
import schemas
import models
from modules import summary_f

router = APIRouter(
    prefix='/text',
    tags=['texts']
)

@router.post('/new_text')
def add_text(request: schemas.Text, db: Session = Depends(get_db)):

    existing_text = db.query(models.Summaries).filter(
        models.Summaries.text == request.text).first()
    if existing_text:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Text exist.")
    
    new_text = models.Summaries(**request.model_dump())
    db.add(new_text)
    db.commit()
    db.refresh(new_text)
    return {"status": "create text success!"}

@router.post('/new_text_with_summary')
def add_text(request: schemas.textCreate, r: Request, db: Session = Depends(get_db)):

    summary_text = summary_f(r.app.state.model, request.text_summaries)

    new_text = models.Summaries(
        text=request.text_summaries,
        text_sum=summary_text, 
    )
    db.add(new_text)
    db.commit()
    db.refresh(new_text)
    return {"status": "create text success!"}
