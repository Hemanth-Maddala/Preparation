// Conditional rendering: showing different UI depending on state.
// Three common patterns: ternary, &&, and if/else before return.

import { useState } from "react";

function Dashboard() {
  return <div className="card">Dashboard content</div>;
}

function Login() {
  return <div className="card">Please log in first</div>;
}

// Pattern 3: if/else logic before the return
function renderContent(isLoggedIn) {
  if (isLoggedIn) return <Dashboard />;
  return <Login />;
}

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <div className="container">
      <button onClick={() => setIsLoggedIn(!isLoggedIn)}>
        {isLoggedIn ? "Logout" : "Login"}
      </button>

      {/* Pattern 1: ternary — render one of two things */}
      <h3>Ternary:</h3>
      {isLoggedIn ? <Dashboard /> : <Login />}

      {/* Pattern 2: && — render only when the condition is true */}
      <h3>&amp;&amp; :</h3>
      {isLoggedIn && <p className="success">You are logged in</p>}

      {/* Pattern 3: function with if/else */}
      <h3>if/else:</h3>
      {renderContent(isLoggedIn)}
    </div>
  );
}

export default App;
