// localStorage — persist state across page refreshes.
// setItem / getItem / removeItem (all string-based).

import { useState, useEffect } from "react";

const STORAGE_KEY = "savedName";

function App() {
  // Lazy initializer: read once when the component first loads
  const [name, setName] = useState(() => localStorage.getItem(STORAGE_KEY) || "");

  // Save to localStorage whenever name changes
  useEffect(() => {
    localStorage.setItem(STORAGE_KEY, name);
  }, [name]);

  return (
    <div className="container">
      <h1>localStorage</h1>

      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Type your name"
      />

      <p>Stored value: <strong>{localStorage.getItem(STORAGE_KEY) || "(empty)"}</strong></p>

      <button
        onClick={() => {
          localStorage.removeItem(STORAGE_KEY);
          setName("");
        }}
      >
        Clear storage
      </button>

      <p>Refresh the page — the name stays!</p>
    </div>
  );
}

export default App;
