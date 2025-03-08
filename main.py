from fastapi import FastAPI

app = FastAPI()

@app.get("/user/")
async def get_user(name: str, age: int):
    return {"name": name, "age": age}
