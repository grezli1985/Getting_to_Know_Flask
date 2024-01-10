from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from project.seminar.lesson_05.D_Z.models import Movie


app = FastAPI()
templates = Jinja2Templates(directory='project/seminar/lesson_05/D_Z/templates')
movies: list[Movie] = []


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        'index.html', {'request': request, 'movies': movies}
    )


@app.get('/kino/', response_class=HTMLResponse)
async def kino(request: Request):
    return templates.TemplateResponse(
        'movie.html', {'request': request, 'movies': movies}
    )


@app.get('/movies/{genre}')
async def get_movies(genre: str):
    list_movies = [movie for movie in movies if movie.genre == genre.title()]
    return list_movies


@app.post('/movies/')
async def create_movie(movie: Movie):
    movies.append(movie)
    return movie
