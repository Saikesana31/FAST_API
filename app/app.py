from fastapi import FastAPI

app =FastAPI()



# create endpoints for the api

@app.get("/hello")
def hello():
    return {"message": "Hello World"}

