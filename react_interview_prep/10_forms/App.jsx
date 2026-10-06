// A basic form: name, email, password, submit.
// One state object + one onChange handler for all inputs.

import { useState } from "react";

function App() {
  const [form, setForm] = useState({ name: "", email: "", password: "" });

  // The `name` attribute tells us which field to update
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submitted:", form);
  };

  return (
    <form onSubmit={handleSubmit} className="container">
      <h1>Basic Form</h1>

      <input
        name="name"
        value={form.name}
        onChange={handleChange}
        placeholder="Name"
      />
      <input
        name="email"
        type="email"
        value={form.email}
        onChange={handleChange}
        placeholder="Email"
      />
      <input
        name="password"
        type="password"
        value={form.password}
        onChange={handleChange}
        placeholder="Password"
      />

      <button type="submit">Submit</button>
    </form>
  );
}

export default App;
