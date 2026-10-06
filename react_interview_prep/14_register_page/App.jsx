// REGISTER PAGE — name, email, password, confirm password.
// Validation: required, password length, passwords match.

import { useState } from "react";

function App() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const [errors, setErrors] = useState({});
  const [success, setSuccess] = useState(false);

  // One handler for all four fields (name attribute selects the field)
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const validate = () => {
    const errs = {};
    if (!form.name) errs.name = "Name is required";
    if (!form.email) {
      errs.email = "Email is required";
    } else if (!/^\S+@\S+\.\S+$/.test(form.email)) {
      errs.email = "Invalid email format";
    }
    if (!form.password) {
      errs.password = "Password is required";
    } else if (form.password.length < 6) {
      errs.password = "Password must be at least 6 characters";
    }
    if (form.password !== form.confirmPassword) {
      errs.confirmPassword = "Passwords do not match";
    }
    return errs;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const errs = validate();
    setErrors(errs);
    if (Object.keys(errs).length > 0) return;
    setSuccess(true);
  };

  if (success) {
    return <div className="container"><h2 className="success">Registration successful!</h2></div>;
  }

  return (
    <form onSubmit={handleSubmit} className="container">
      <h1>Register</h1>

      <input name="name" value={form.name} onChange={handleChange} placeholder="Name" />
      {errors.name && <p className="error">{errors.name}</p>}

      <input name="email" value={form.email} onChange={handleChange} placeholder="Email" />
      {errors.email && <p className="error">{errors.email}</p>}

      <input name="password" type="password" value={form.password} onChange={handleChange} placeholder="Password" />
      {errors.password && <p className="error">{errors.password}</p>}

      <input name="confirmPassword" type="password" value={form.confirmPassword} onChange={handleChange} placeholder="Confirm password" />
      {errors.confirmPassword && <p className="error">{errors.confirmPassword}</p>}

      <button type="submit">Register</button>
    </form>
  );
}

export default App;
