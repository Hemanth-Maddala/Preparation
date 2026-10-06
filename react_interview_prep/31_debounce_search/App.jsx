// Debounce: wait until the user stops typing, THEN act.
// setTimeout starts a timer; the cleanup clears the previous one,
// so only the LAST keystroke's timer survives.

import { useEffect, useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [debounced, setDebounced] = useState("");
  const [result, setResult] = useState("");

  // 1. Debounce the raw query into `debounced` after 500ms of no typing
  useEffect(() => {
    const timer = setTimeout(() => setDebounced(query), 500);
    return () => clearTimeout(timer); // cancel the previous timer
  }, [query]);

  // 2. Perform the "search" only when the debounced value changes
  useEffect(() => {
    if (debounced) setResult(`Searching for "${debounced}"...`);
  }, [debounced]);

  return (
    <div className="container">
      <h1>Debounce Search</h1>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Type to search"
      />

      <p>Raw input: {query}</p>
      <p>Debounced (after 500ms): {debounced}</p>
      <p className="success">{result}</p>
    </div>
  );
}

export default App;
