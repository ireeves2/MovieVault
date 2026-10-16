from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="MovieVault API", version="0.1.0")

api_key = os.getenv("TMDB_API_KEY")
rat = os.getenv("TMDB_RAT")

# Allow the React dev server to call this API during local development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"status": "MovieVault API is running"}


# --- Feature: Movie Search -------------------------------------------------
@app.get("/api/search")
def search_movies(query: str = ""):
    # TODO: call TMDB /search/movie
    result = requests.get(
    "https://api.themoviedb.org/3/search/movie",
    headers={
        "Authorization": f"Bearer {rat}",
        "accept": "application/json",
    },
    params={"query": query},
    timeout=10,)
    return {"query": query, "results": result.json()}


# --- Feature: Movie Details --------------------------------------------------
@app.get("/api/movies/{movie_id}")
def get_movie_details(movie_id: int):
    # TODO: call TMDB /movie/{movie_id}
    return {"id": movie_id, "title": None, "genres": [], "cast": []}


# --- Feature: Recommendations -----------------------------------------------
@app.get("/api/movies/{movie_id}/recommendations")
def get_recommendations(movie_id: int):
    # TODO: call TMDB /movie/{movie_id}/recommendations
    return {"movie_id": movie_id, "recommendations": []}


# --- Feature: Watch Providers ------------------------------------------------
@app.get("/api/movies/{movie_id}/watch-providers")
def get_watch_providers(movie_id: int, country: str = "US"):
    # TODO: call TMDB /movie/{movie_id}/watch/providers
    return {"movie_id": movie_id, "country": country, "providers": {}}


# --- Feature: Watchlist -------------------------------------------------------
watchlist_store = []  # TODO: replace with SQLite-backed storage


@app.get("/api/watchlist")
def get_watchlist():
    return {"watchlist": watchlist_store}


@app.post("/api/watchlist/{movie_id}")
def add_to_watchlist(movie_id: int):
    if movie_id not in watchlist_store:
        watchlist_store.append(movie_id)
    return {"watchlist": watchlist_store}


@app.delete("/api/watchlist/{movie_id}")
def remove_from_watchlist(movie_id: int):
    if movie_id in watchlist_store:
        watchlist_store.remove(movie_id)
    return {"watchlist": watchlist_store}
