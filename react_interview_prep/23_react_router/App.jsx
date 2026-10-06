// React Router basics: BrowserRouter → Routes → Route → Link.
// In a real app BrowserRouter usually wraps the app in main.jsx;
// here it lives inside App.jsx so this example is self-contained.

import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./Home.jsx";
import About from "./About.jsx";
import Login from "./Login.jsx";

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> | <Link to="/about">About</Link> |{" "}
        <Link to="/login">Login</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
