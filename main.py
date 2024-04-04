from contextlib import asynccontextmanager

from dotenv import load_dotenv
load_dotenv('.env', override=True)

import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import text
from database.database import engine
import models
import uvicorn
import google.generativeai as genai

genai.configure(api_key="AIzaSyDpkEooxN0JhFewtRdDWnrk_JBAjXx7BrU")

models.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = genai.GenerativeModel('gemini-pro')
    yield
    app.state.model.clear()

app = FastAPI(lifespan=lifespan)

app.include_router(text.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
