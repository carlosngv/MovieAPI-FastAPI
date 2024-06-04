from typing import List

from fastapi import APIRouter, Path, Query, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from config.database import Session
from models.movie import MovieTable
from schemes.movie import Movie
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
movie_router = APIRouter()

# @movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content={'movies': jsonable_encoder(result)})

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie: # ? Que el id del path sea mayor o igual a 1 y menor o igual a 2000
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'msg': 'Movie not found'})

    return JSONResponse(status_code=200, content={'movie': jsonable_encoder(result)})

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> dict:
    db = Session()
    result = MovieService(db).get_movie_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'msg': 'Movie not found'})
    return JSONResponse(content={'movie': jsonable_encoder(result)})


@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    resp = {
        'message': 'Se ha registrado la película'
    }
    return JSONResponse(content=resp, status_code=201)

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).update_movie(id, movie)
    if not result:
        return JSONResponse(content={'message': 'Movie not found'}, status_code=400)

    return JSONResponse(content={'message': 'Movie successfully updated'}, status_code=201)

@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict)
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieService(db).delete_movie(id)
    if not result:
        return JSONResponse(content={'message': 'Movie not found'}, status_code=400)

    return JSONResponse(content={'message': 'Movie successfully deleted'}, status_code=200)
