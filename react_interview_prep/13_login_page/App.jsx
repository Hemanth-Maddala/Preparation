// LOGIN PAGE — the most common React interview task.
// Everything here is easy to reproduce from memory.
// Demo credentials: test@test.com / password

import { useState } from "react";

// Fake login that returns a Promise, simulating a real API call
const fakeLogin = (email, password) =>
  new Promise((resolve, reject) => {
    setTimeout(() => {
      if (email === "test@test.com" && password === "password") {
        resolve({ token: "fake-token", name: "Hemanth" });
      } else {
        reject(new Error("Invalid email or password"));
      }
    }, 1000);
  });

function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [user, setUser] = useState(null);

  const validate = () => {
    const errs = {};
    if (!email) errs.email = "Email is required";
    if (!password) errs.password = "Password is required";
    return errs;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // 1. Validate
    const errs = validate();
    setErrors(errs);
    if (Object.keys(errs).length > 0) return;

    // 2. Loading + call the fake API
    setLoading(true);
    setError("");
    try {
      const data = await fakeLogin(email, password);
      setUser(data); // success
    } catch (err) {
      setError(err.message); // error
    } finally {
      setLoading(false);
    }
  };

  // Success screen
  if (user) {
    return (
      <div className="container">
        <h2>Welcome, {user.name}!</h2>
        <p className="success">You logged in successfully.</p>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} className="container">
      <h1>Login</h1>

      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      {errors.email && <p className="error">{errors.email}</p>}

      <input
        type={showPassword ? "text" : "password"}
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button type="button" onClick={() => setShowPassword(!showPassword)}>
        {showPassword ? "Hide" : "Show"} password
      </button>
      {errors.password && <p className="error">{errors.password}</p>}

      {error && <p className="error">{error}</p>}

      <button type="submit" disabled={loading}>
        {loading ? "Logging in..." : "Login"}
      </button>
    </form>
  );
}

export default App;
