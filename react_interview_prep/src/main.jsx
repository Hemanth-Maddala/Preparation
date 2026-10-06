// Standard Vite + React entry point.
// Note: StrictMode is intentionally NOT used so render counts
// stay predictable while practicing (StrictMode double-runs effects in dev).

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
