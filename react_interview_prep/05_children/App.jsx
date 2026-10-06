// props.children: content placed between the opening and closing
// tags of a component becomes available as `children`.

import Card from "./Card.jsx";

function App() {
  return (
    <div className="container">
      {/* Everything inside <Card>...</Card> is passed as children */}
      <Card>
        <h2>Hello</h2>
        <p>This content is passed as props.children.</p>
      </Card>

      <Card>
        <h2>Another card</h2>
        <p>Same layout, different content.</p>
      </Card>
    </div>
  );
}

export default App;
