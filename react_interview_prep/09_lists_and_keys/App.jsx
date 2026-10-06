// Lists and keys: converting an array into an array of JSX with map.

const users = [
  { id: 1, name: "Hemanth" },
  { id: 2, name: "Ravi" },
  { id: 3, name: "Anu" },
];

function App() {
  return (
    <div className="container">
      <h1>Lists and Keys</h1>
      <ul>
        {/* key must be unique and stable (an id, not the array index).
            React uses it to track items when the list changes. */}
        {users.map((user) => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>

      <p>
        Try changing key={user.id} to key={index} and think about what
        breaks when you reorder or delete items.
      </p>
    </div>
  );
}

export default App;
