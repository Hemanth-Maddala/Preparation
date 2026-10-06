// Controlled components: React state is the single source of truth.
// The input only shows what state says, and onChange keeps them in sync.

import { useState } from "react";

function App() {
  const [name, setName] = useState("");

  return (
    <div className="container">
      <h1>Controlled Components</h1>

      {/* CONTROLLED: value comes from state, changes go back to state */}
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Controlled input"
      />
      <p>State: {name}</p>

      {/* UNCONTROLLED: the DOM owns the value; React never sees it */}
      <input defaultValue="" placeholder="Uncontrolled input" />
      <p>Note: the uncontrolled input cannot be read by React until you use a ref.</p>
    </div>
  );
}

export default App;
