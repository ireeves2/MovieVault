"""
MovieVault backend — FastAPI entrypoint.

This is a starter scaffold. Each route below corresponds to a planned
MVP feature / GitHub Issue and currently returns placeholder data.
Replace the placeholders with real TMDB API calls as you build each
feature on its own branch.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MovieVault API", version="0.1.0")

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
    return {"query": query, "results": []}


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
