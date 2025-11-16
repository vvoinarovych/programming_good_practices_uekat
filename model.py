from pydantic import BaseModel
from typing import List


class Movie(BaseModel):
    movieId: int
    title: str
    genres: str


class Link(BaseModel):
    movieId: int
    imdbId: str
    tmdbId: int


class Rating(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: int


class Tag(BaseModel):
    userId: int
    movieId: int
    tag: str
    timestamp: int
