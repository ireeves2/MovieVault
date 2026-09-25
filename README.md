# 🎬 MovieVault

A movie discovery, recommendation, and watchlist app that also shows where each
movie is currently available to stream, rent, or buy — powered by the
[TMDB API](https://www.themoviedb.org/documentation/api) (watch-provider data
supplied via TMDB's partnership with JustWatch).

> Built as part of a "Growing a Competency" assignment to learn Git & GitHub
> collaborative workflows (branches, commits, pull requests, Issues, and
> GitHub Actions).

## Why this project?

Streaming availability changes constantly — a movie you want to rewatch might
have moved services since you last checked. MovieVault solves that by pulling
live watch-provider data instead of relying on memory or a single service's
catalog.

## Planned MVP Features

- [ ] Movie search
- [ ] Movie details (poster, synopsis, genres, rating, runtime, cast/crew)
- [ ] Recommendations based on a selected movie
- [ ] Personal watchlist (add/remove)
- [ ] "Where to watch" (stream / rent / buy, by country)

## Tech Stack

| Layer        | Choice            |
|--------------|-------------------|
| Frontend     | React             |
| Backend      | Python + FastAPI  |
| Database     | SQLite            |
| External API | TMDB              |
| CI/CD        | GitHub Actions    |

## Project Structure

```
MovieVault/
├── backend/          # FastAPI app
│   ├── app/
│   │   └── main.py
│   └── requirements.txt
├── frontend/         # React app
│   ├── src/
│   └── public/
├── docs/
│   └── learning-log.md
└── .github/workflows/ # CI
```

## Getting Started

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env          # then add your TMDB_API_KEY
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## Attribution

This product uses the TMDB API but is not endorsed or certified by TMDB.
Watch-provider data is supplied by JustWatch.

## Development Workflow

This project is being built using a feature-branch + pull-request workflow:

```
Issue → feature/<name> branch → commits → push → Pull Request → merge to main
```

See open Issues for the current roadmap.

## Status

🚧 Early scaffold — core features not yet implemented. See `docs/learning-log.md`
for the Git/GitHub learning process behind this project.
