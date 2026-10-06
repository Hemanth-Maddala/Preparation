// Pagination: `page` state + `slice()` to show one page at a time.

import { useState } from "react";

const items = Array.from({ length: 50 }, (_, i) => `Item ${i + 1}`);
const PAGE_SIZE = 5;

function App() {
  const [page, setPage] = useState(1);

  const totalPages = Math.ceil(items.length / PAGE_SIZE);

  // slice(start, end) gives the items for the current page
  const pageItems = items.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE);

  return (
    <div className="container">
      <h1>Pagination</h1>

      <ul>
        {pageItems.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>

      <button onClick={() => setPage(page - 1)} disabled={page === 1}>
        Previous
      </button>
      <span> Page {page} / {totalPages} </span>
      <button onClick={() => setPage(page + 1)} disabled={page === totalPages}>
        Next
      </button>
    </div>
  );
}

export default App;
