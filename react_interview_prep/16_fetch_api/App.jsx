// Fetching API data with fetch() + useEffect.
// Empty dependency array = fetch once on mount.

import { useState, useEffect } from "react";

function App() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((res) => res.json())     // parse JSON from the response
      .then((data) => {
        setPosts(data);              // save to state
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []); // empty deps: run once on mount

  if (loading) return <div className="container">Loading...</div>;

  return (
    <div className="container">
      <h1>Posts</h1>
      <ul>
        {posts.slice(0, 5).map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
