from fastapi import FastAPI

app = FastAPI()


@app.get("/")

def index():
    return {"message":"xuxuzinho bobinho te ama mtmtmt"}
