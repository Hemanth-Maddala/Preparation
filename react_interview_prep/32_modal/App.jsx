// Modal: conditional rendering + event handling + composition.

import { useState } from "react";

// Reusable modal. Renders nothing when closed.
function Modal({ isOpen, onClose }) {
  if (!isOpen) return null; // conditional rendering

  return (
    <div className="overlay" onClick={onClose}>
      {/* stopPropagation: clicking INSIDE the modal must not close it */}
      <div className="modal" onClick={(e) => e.stopPropagation()}>
        <h2>Modal</h2>
        <p>Click outside the box or the Close button to dismiss.</p>
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
}

function App() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="container">
      <h1>Modal</h1>
      <button onClick={() => setIsOpen(true)}>Open modal</button>
      <Modal isOpen={isOpen} onClose={() => setIsOpen(false)} />
    </div>
  );
}

export default App;
