// JSX: HTML-like syntax inside JavaScript.
// Anything in {} is a JavaScript expression evaluated at render time.

function App() {
  const name = "Hemanth";
  const age = 22;
  const isDeveloper = true;
  const items = ["React", "JSX", "Hooks"];
  const today = new Date().toLocaleDateString();

  return (
    <div className="container">
      {/* 1. Output a variable inside JSX with {} */}
      <h1>Hello {name}</h1>

      {/* 2. Any JS expression works inside {} */}
      <p>Age next year: {age + 1}</p>

      {/* 3. Ternary expression */}
      <p>{isDeveloper ? "Yes, I am a developer" : "No"}</p>

      {/* 4. className, not class */}
      <div className="card">Styled with className</div>

      {/* 5. Calling a function inside JSX */}
      <p>Today: {today}</p>

      {/* 6. Rendering a list (map must return JSX) */}
      <ul>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>

      {/* 7. Fragment: group elements without a wrapper div */}
      <>
        <p>Fragment element 1</p>
        <p>Fragment element 2</p>
      </>
    </div>
  );
}

export default App;
