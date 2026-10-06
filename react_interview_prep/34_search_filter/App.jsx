// Search + filter: an input drives a `filter()` over a list.

import { useState } from "react";

const users = ["Hemanth", "Ravi", "Anu", "Priya", "Kiran", "Sneha"];

function App() {
  const [search, setSearch] = useState("");

  // filter returns only items that match (case-insensitive)
  const filtered = users.filter((name) =>
    name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="container">
      <h1>Search Filter</h1>

      <input
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search users"
      />

      {filtered.length === 0 ? (
        <p>No results for "{search}"</p>
      ) : (
        <ul>
          {filtered.map((name) => (
            <li key={name}>{name}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
