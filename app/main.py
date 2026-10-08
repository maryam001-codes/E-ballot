from fastapi import FastAPI

app = FastAPI(title="E-Ballot")


@app.get("/")
def home():
    return {"message": "E-Ballot API is running"}