from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Name":"Usman Malik",
            "Title":"Junior ML Engineer"}

