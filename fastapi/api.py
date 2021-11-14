from fastapi import FastAPI
app =FastAPI()

#request followed by the url
@app.get("/")
async def root():
    return {"welcome to fastapi"}

    o#post method follewed buy the url

@app.get("/posts")
def get_post():
    return{"data":"this is my post methehod"}

@app.post("/createposts")
def create_post():
    return{"message":"post successfully created"}