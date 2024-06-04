
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from routers.movie import movie_router
from routers.auth import auth_router
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler

app = FastAPI()
app.title = 'My movie API'
app.version = '0.0.1'
Base.metadata.create_all(bind=engine)

app.add_middleware(ErrorHandler)
app.include_router(auth_router)
app.include_router(movie_router)


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('''
        <h1>Hello World</h1>
    ''')
