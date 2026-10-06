// Navigation: useNavigate for programmatic navigation (e.g. after login),
// Link for user-click navigation.

import { BrowserRouter, Routes, Route, Link, useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate(); // programmatic navigation

  const handleLogin = () => {
    // Imagine validation + API call happen here...
    navigate("/dashboard");       // then redirect
  };

  return (
    <div>
      <h2>Login page</h2>
      <button onClick={handleLogin}>Login → navigate("/dashboard")</button>
      <p>
        Or click <Link to="/">this Link</Link> — Link renders an anchor.
      </p>
    </div>
  );
}

function Dashboard() {
  return <h2>Dashboard (after login)</h2>;
}

function Home() {
  return <h2>Home</h2>;
}

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> | <Link to="/login">Login</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
