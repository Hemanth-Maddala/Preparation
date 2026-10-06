// Protected route: redirect to /login when the user is not authenticated.
// This is a VERY common practical interview topic.

import { BrowserRouter, Routes, Route, Link, useNavigate, Navigate } from "react-router-dom";
import { useState } from "react";

// The wrapper: if not authenticated, redirect; otherwise render children.
function ProtectedRoute({ isAuth, children }) {
  if (!isAuth) return <Navigate to="/login" replace />;
  return children;
}

function Login({ onLogin }) {
  const navigate = useNavigate();

  const handleLogin = () => {
    onLogin();               // set auth state in App
    navigate("/dashboard");  // go to the protected page
  };

  return (
    <div>
      <h2>Login</h2>
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

function Dashboard() {
  return <h2>Dashboard (protected)</h2>;
}

function App() {
  const [isAuth, setIsAuth] = useState(false);

  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> | <Link to="/login">Login</Link> |{" "}
        <Link to="/dashboard">Dashboard</Link>
      </nav>

      <Routes>
        <Route path="/" element={<h2>Home</h2>} />
        <Route path="/login" element={<Login onLogin={() => setIsAuth(true)} />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute isAuth={isAuth}>
              <Dashboard />
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
