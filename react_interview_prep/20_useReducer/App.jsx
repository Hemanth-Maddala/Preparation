// useReducer — manage state with a pure reducer function and actions.
// dispatch({ type: "..." }) tells the reducer HOW to update state.
// You should use useReducer when your state consists of multiple sub-values, when the next state depends heavily on the previous state, or when different user actions update the same state in various ways

import { useReducer } from "react";

// reducer: a pure function (state, action) => newState
function reducer(state, action) {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    case "reset":
      return { count: 0 };
    default:
      return state;
  }
}

function App() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <div className="container">
      <h1>useReducer</h1>
      <h2>Count: {state.count}</h2>
      <button onClick={() => dispatch({ type: "increment" })}>+</button>
      <button onClick={() => dispatch({ type: "decrement" })}>-</button>
      <button onClick={() => dispatch({ type: "reset" })}>Reset</button>
    </div>
  );
}

export default App;
