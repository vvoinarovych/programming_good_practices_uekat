import csv
from typing import List
from model import Movie, Link, Rating, Tag
from fastapi import FastAPI
from typing import List


def load_movies() -> List[Movie]:
    movies = []
    with open('files/movies.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Wczytujemy dane z CSV i tworzymy obiekt Movie
            movie = Movie(
                movieId=int(row["movieId"]),
                title=row["title"],
                genres=row["genres"]
            )
            movies.append(movie)
    return movies


def load_links() -> List[Link]:
    links = []
    with open('files/links.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tmdbId = row["tmdbId"]
            tmdbId = int(tmdbId) if tmdbId else 0

            link = Link(
                movieId=int(row["movieId"]),
                imdbId=row["imdbId"],
                tmdbId=tmdbId
            )
            links.append(link)
    return links



def load_ratings() -> List[Rating]:
    ratings = []
    with open('files/ratings.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rating = Rating(
                userId=int(row["userId"]),
                movieId=int(row["movieId"]),
                rating=float(row["rating"]),
                timestamp=int(row["timestamp"])
            )
            ratings.append(rating)
    return ratings


def load_tags() -> List[Tag]:
    tags = []
    with open('files/tags.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tag = Tag(
                userId=int(row["userId"]),
                movieId=int(row["movieId"]),
                tag=row["tag"],
                timestamp=int(row["timestamp"])
            )
            tags.append(tag)
    return tags


app = FastAPI()


@app.get("/movies", response_model=List[Movie])
def get_movies():
    movies = load_movies()
    return movies


@app.get("/links", response_model=List[Link])
def get_links():
    links = load_links()
    return links


@app.get("/ratings", response_model=List[Rating])
def get_ratings():
    ratings = load_ratings()
    return ratings


@app.get("/tags", response_model=List[Tag])
def get_tags():
    tags = load_tags()
    return tags
