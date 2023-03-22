from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel



app = FastAPI()

@app.get('/')
def index():
    return { 'data': { 'name': 'Okusa' } }

@app.get('/blog')
def index(limit=10, published:bool = True, sort: Optional[str] = None):
    if published:
        return { 'data': f'{limit} published blogs from db' }
    else:
        return { 'data': f'{limit} blogs from db' }

@app.get('/about')
def about():
    return { 'data': 'about page' }

@app.get('/blog/unpublished')
def unpublished():
    
    return { 'data': 'unpublished blogs' }

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog post with id = id
    return { 'data': id }

@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments from blog post where id = id
    return { 'data': f'Comments from blog post {id}' }


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    
    return {'data': {'message': f'Blog is created with title as {request.title}'}}

