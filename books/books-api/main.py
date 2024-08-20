from fastapi import FastAPI

app =FastAPI()

@app.get("/")
def get_root():
  return {"message": "Hello World , I come in peace"}