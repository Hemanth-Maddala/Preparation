// API CRUD with fetch: GET, POST, PUT, DELETE against jsonplaceholder.

import { useState, useEffect } from "react";

const API = "https://jsonplaceholder.typicode.com/posts";

function App() {
  const [posts, setPosts] = useState([]);
  const [title, setTitle] = useState("");

  // READ (GET)
  useEffect(() => {
    fetch(API)
      .then((r) => r.json())
      .then(setPosts);
  }, []);

  // CREATE (POST)
  const createPost = async (e) => {
    e.preventDefault();
    const res = await fetch(API, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, userId: 1 }),
    });
    const newPost = await res.json();
    setPosts([newPost, ...posts]); // add to the local list
    setTitle("");
  };

  // UPDATE (PUT)
  const updatePost = async (post) => {
    const res = await fetch(`${API}/${post.id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ...post, title: post.title + " (updated)" }),
    });
    const updated = await res.json();
    setPosts(posts.map((p) => (p.id === updated.id ? updated : p)));
  };

  // DELETE (DELETE)
  const deletePost = async (id) => {
    await fetch(`${API}/${id}`, { method: "DELETE" });
    setPosts(posts.filter((p) => p.id !== id)); // remove locally
  };

  return (
    <div className="container">
      <h1>API CRUD</h1>

      <form onSubmit={createPost}>
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="New post title"
        />
        <button type="submit">Create</button>
      </form>

      <ul>
        {posts.slice(0, 10).map((post) => (
          <li key={post.id}>
            {post.title}
            <button onClick={() => updatePost(post)}>Edit</button>
            <button onClick={() => deletePost(post.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
