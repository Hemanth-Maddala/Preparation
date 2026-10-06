// Event handling: onClick, onChange, onSubmit.
// Handlers are passed as functions (not called), and they receive
// the synthetic event object `e`.

import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [submitted, setSubmitted] = useState("");

  // onClick — pass the function reference
  const handleClick = () => alert("Button clicked");

  // onChange — the event object gives access to the input value
  const handleChange = (e) => setText(e.target.value);

  // onSubmit — always preventDefault to stop the page reload
  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(text);
  };

  return (
    <div className="container">
      <h1>Event Handling</h1>

      <button onClick={handleClick}>Click me (onClick)</button>

      <input
        type="text"
        value={text}
        onChange={handleChange}
        placeholder="Type here (onChange)"
      />

      <form onSubmit={handleSubmit}>
        <button type="submit">Submit (onSubmit)</button>
      </form>

      {submitted && <p className="success">Submitted: {submitted}</p>}
    </div>
  );
}

export default App;
