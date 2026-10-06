// Auth flow: Login → store auth → navigate → protected page → Logout.
// Login persists to localStorage (DEMO only — not production auth).

import { BrowserRouter, Routes, Route, Link, Navigate, useNavigate } from "react-router-dom";
import { useState } from "react";

// Fake login that returns a Promise
const fakeLogin = () =>
  new Promise((resolve) =>
    setTimeout(() => resolve({ token: "demo-token", name: "Hemanth" }), 800)
  );

function App() {
  // Lazy init: read auth from localStorage on first load
  const [user, setUser] = useState(() =>
    JSON.parse(localStorage.getItem("auth"))
  );

  const login = async () => {
    const data = await fakeLogin();
    localStorage.setItem("auth", JSON.stringify(data)); // persist
    setUser(data);
  };

  const logout = () => {
    localStorage.removeItem("auth"); // clear
    setUser(null);
  };

  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> |{" "}
        {user ? (
          <button onClick={logout}>Logout ({user.name})</button>
        ) : (
          <Link to="/login">Login</Link>
        )}
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login onLogin={login} />} />
        <Route
          path="/dashboard"
          element={user ? <Dashboard user={user} /> : <Navigate to="/login" replace />}
        />
      </Routes>
    </BrowserRouter>
  );
}

function Home() {
  return <h2>Home</h2>;
}

function Login({ onLogin }) {
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await onLogin();       // fake API + save
    navigate("/dashboard");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input placeholder="Email" />
      <input type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  );
}

function Dashboard({ user }) {
  return (
    <div>
      <h2>Dashboard (protected)</h2>
      <p>Welcome, {user.name}! Refresh the page — you stay logged in.</p>
    </div>
  );
}

export default App;
