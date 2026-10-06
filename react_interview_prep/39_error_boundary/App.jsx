// Error Boundary — the ONE place a class component is still normal.
// It catches errors thrown during rendering of its children.

import React, { useState } from "react";

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  // Called when a child throws during render
  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error, info) {
    console.log("Caught:", error, info);
  }

  render() {
    if (this.state.hasError) {
      return <h2>Something went wrong.</h2>;
    }
    return this.props.children;
  }
}

function Boom() {
  throw new Error("Boom!");
}

function App() {
  const [broken, setBroken] = useState(false);

  return (
    <div className="container">
      <h1>Error Boundary</h1>
      <ErrorBoundary>
        {broken ? <Boom /> : <p>Working fine. Click the button to crash.</p>}
      </ErrorBoundary>
      <button onClick={() => setBroken(true)}>Make it crash</button>
    </div>
  );
}

export default App;
