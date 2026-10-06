// Props: data passed into a component from its parent.
// props is just an object: { name: "Hemanth", age: 22 }

// Variant 1: read from the `props` object
function User(props) {
  return (
    <div className="card">
      <h3>{props.name}</h3>
      <p>Age: {props.age}</p>
    </div>
  );
}

// Variant 2: destructure props (cleaner, very common in interviews)
function UserDestructured({ name, age }) {
  return (
    <div className="card">
      <h3>{name}</h3>
      <p>Age: {age}</p>
    </div>
  );
}
   
function App() {
  return (
    <div className="container">
      <h1>Props</h1>
      <User name="Hemanth" age={22} />
      <User name="Ravi" age={25} />
      <User name="Anu" age={21} />
      <UserDestructured name="Priya" age={24} />
    </div>
  );
}

export default App;
