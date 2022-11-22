from typing import List
from fastapi import Depends, FastAPI, HTTPException,Request
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import crud, models,security
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from jwt import decodeJWT
import re

from schemas import UserCreateSchema, UserSchema, TokenSchema


ACCESS_TOKEN_EXPIRE_MINUTES = 30


models.Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI()


origins = "*"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/heathckeck")
async def heathckeck() -> dict:
    return {"message": 'ok'}


# @app.post("/login/", response_model=UserSchema)
# def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_username(db, username=user.username)
#     if db_user:
#         if (security.verify_hash(user.password, db_user.salt).decode('utf-8') == db_user.password):
#             return db_user
    
#     raise HTTPException(status_code=400, detail="Invalid Login")

@app.post("/login", response_model=TokenSchema)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    db_user = crud.get_user_by_username(db, username=form_data.username)
    if not (security.verify_hash(form_data.password, db_user.salt).decode('utf-8') == db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token}