from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API is running successfully"}

@app.get("/quiz")
def get_quiz():
    return {
        "question": "What is ก?",
        "choices": ["ko kai", "kho khai", "ngo ngu", "cho chan"],
        "answer": "ko kai"
    }
