from typing import List
from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
import crud, models,security
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from datetime import timedelta

from schemas import TokenSchema, PostSchema, LoginSchema


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


from jwt import JWTBearer
@app.get("/posts", dependencies=[Depends(JWTBearer())])
async def get_posts(db: Session = Depends(get_db)):
    return crud.get_all_posts(db)


@app.post("/login", response_model=TokenSchema)
async def login_for_access_token(request:LoginSchema, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=request.username)
    if db_user is None or not (security.verify_hash(request.password, db_user.salt).decode('utf-8') == db_user.password):
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


@app.get("/post/{post_id}", dependencies=[Depends(JWTBearer())], response_model=PostSchema)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return crud.get_post(db=db, post_id=post_id)

