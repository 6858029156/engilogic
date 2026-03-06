from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, SessionLocal
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/start/{nickname}")
def start_quiz(nickname: str):
    db = SessionLocal()

    user = db.query(models.User).filter(models.User.nickname == nickname).first()

    if not user:
        user = models.User(nickname=nickname, counter=1)
        db.add(user)
    else:
        user.counter += 1

    db.commit()
    db.refresh(user)
    db.close()

    return {"nickname": nickname, "counter": user.counter}
