// Form validation with plain React state — no libraries.
// Validate on submit, show errors, only proceed when valid.

import { useState } from "react";

function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});

  const validate = () => {
    const errs = {};
    if (!email) {
      errs.email = "Email is required";
    } else if (!/^\S+@\S+\.\S+$/.test(email)) {
      errs.email = "Invalid email format";
    }
    if (!password) {
      errs.password = "Password is required";
    } else if (password.length < 6) {
      errs.password = "Password must be at least 6 characters";
    }
    return errs;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const errs = validate();
    setErrors(errs);
    // Stop here if anything failed
    if (Object.keys(errs).length > 0) return;
    alert("Form is valid — submitting!");
  };

  return (
    <form onSubmit={handleSubmit} className="container">
      <h1>Form Validation</h1>

      <input
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      {errors.email && <p className="error">{errors.email}</p>}

      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password (min 6 chars)"
      />
      {errors.password && <p className="error">{errors.password}</p>}

      <button type="submit">Submit</button>
    </form>
  );
}

export default App;
