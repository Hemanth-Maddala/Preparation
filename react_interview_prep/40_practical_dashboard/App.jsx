// Practical dashboard: combines the patterns from earlier folders —
// props, useState, useEffect, fetch, loading/error, search/filter,
// conditional rendering. No visual complexity.

import { useState, useEffect } from "react";

// Reusable presentational component (props)
function StatCard({ label, value }) {
  return (
    <div className="card">
      <h3>{label}</h3>
      <p className="success">{value}</p>
    </div>
  );
}

function App() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");

  // useEffect + fetch with loading/error
  useEffect(() => {
    const load = async () => {
      try {
        const res = await fetch("https://jsonplaceholder.typicode.com/users");
        if (!res.ok) throw new Error("Failed to load");
        setUsers(await res.json());
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    load();
  }, []);

  // Search/filter derived from state
  const filtered = users.filter((u) =>
    u.name.toLowerCase().includes(search.toLowerCase())
  );

  // Conditional rendering: loading → error → data
  if (loading) return <div className="container">Loading...</div>;
  if (error) return <div className="container"><p className="error">Error: {error}</p></div>;

  return (
    <div className="container">
      <h1>Dashboard</h1>

      <div className="row">
        <StatCard label="Total users" value={users.length} />
        <StatCard label="Filtered" value={filtered.length} />
      </div>

      <input
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search by name"
      />

      {filtered.length === 0 ? (
        <p>No users match "{search}"</p>
      ) : (
        <ul>
          {filtered.map((u) => (
            <li key={u.id}>
              {u.name} — {u.email}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
