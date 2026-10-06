// Component composition: small components inside other components.
// App renders UserCard twice — the same component reused.

import UserCard from "./UserCard.jsx";

function App() {
  return (
    <div className="container">
      <h1>Functional Components</h1>
      <UserCard />
      <UserCard />
    </div>
  );
}

export default App;
