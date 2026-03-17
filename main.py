from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World! FastAPI is awesome."}

@app.get("/candidates/{candidate_id}")
def get_candidate(candidate_id: int):
    return {"candidate_id": candidate_id, "status": "i am alive"}