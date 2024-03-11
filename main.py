from fastapi import FastAPI
from typing import Optional
import uvicorn
app=FastAPI()


@app.get("/blog")
def index(limit,published: bool=True, sort: Optional[str]=None):
    if published:
        return{'data':f'{limit} published blog list'}
    else:
        return {'data':f'{limit} all blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return{'data':'unpublished'}

@app.get("/blog/{id}")
def show(id:int):
    return{'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {"data":{'1','2'}}

@app.post("/blog")
def create(blog:Blog):
    return{'data':f"Blog is created as {{blog.name}}"}


# if __name__=="__main__":
#     uvicorn.run (app, host="127.0.0.1",port=9000)
