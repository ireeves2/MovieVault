import { useState } from "react";

const API_BASE = "http://localhost:8000";

export default function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  async function handleSearch(e) {
    e.preventDefault();
    // TODO: replace with real results once /api/search calls TMDB
    const res = await fetch(`${API_BASE}/api/search?query=${encodeURIComponent(query)}`);
    const data = await res.json();
    setResults(data.results);
  }

  return (
    <div style={{ fontFamily: "sans-serif", maxWidth: 600, margin: "2rem auto" }}>
      <h1>🎬 MovieVault</h1>
      <p>Search, discover, and track where to watch your favorite movies.</p>

      <form onSubmit={handleSearch}>
        <input
          type="text"
          placeholder="Search for a movie..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{ padding: "0.5rem", width: "70%" }}
        />
        <button type="submit" style={{ padding: "0.5rem 1rem" }}>
          Search
        </button>
      </form>

      <ul>
        {results.length === 0 && <li style={{ color: "#888" }}>No results yet — backend is a stub.</li>}
        {results.map((movie) => (
          <li key={movie.id}>{movie.title}</li>
        ))}
      </ul>
    </div>
  );
}
