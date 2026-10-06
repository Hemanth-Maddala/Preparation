// useRef — two uses:
// 1) Reference a DOM node (focus an input).
// 2) Keep a value across renders WITHOUT triggering a re-render.

import { use, useRef, useState } from "react";

function App() {
  const inputRef = useRef(null);    // points at the <input> below
  const countRef = useRef(0);       // persistent value, no re-render
  const [count, setCount] = useState(0);

  const focusInput = () => {
    inputRef.current.focus();
    inputRef.current.select();
  };

  const incrementRef = () => {
    countRef.current += 1;
    console.log("ref count:", countRef.current);
    // Notice: the number on screen never changes — no re-render.
  };

  return (
    <div className="container">
      <h1>useRef</h1>

      <input ref={inputRef} placeholder="Click the button to focus me" />
      <button onClick={focusInput}>Focus input (DOM ref)</button>

      <button onClick={() => setCount(count + 1)}>State count: {count}</button>
      <button onClick={incrementRef}>Ref count: {countRef.current}</button>

      <p className="success">
        Ref count updates do NOT trigger a re-render. Check the console.
      </p>
    </div>
  );
}

export default App;




// Explanation
// 1. useRef -> has mainly two goals -> 1. storing mutable data that doesn't need to trigger a UI update. 2.  interacting with the DOM

// 1. firstly about 1st use  
// 2. means even though when the useRef Variable value changes in the page component , then that value will be changes internally -> like varable.current = changed value, 
// 3. as internally changing (like .current) -> the page will not be re-rendered, so even though the value changes it will not shown in the page
// 4. but when any non userRed variable changes like state variables , we know that page will be re-rendered , so then we can see the changed value of useRef value
// 5. exmaple in above useref-increment button , if clicked it will not show increment , but actually it was incrementing
// 6. when the normal button incremented -> then normal will be incremented (page re-rendered and show) . as page re-rendered , the useref counter shows the changed value.

// 2. DOM Access
// How it works: By passing inputRef to the ref attribute of the <input> element, you are telling React: "Once this element is created in the browser, put the actual DOM node into inputRef.current."
// The Benefit: Usually, React handles the DOM for you. But sometimes you need to use native browser APIs that React doesn't have "state" for, such as:
// Focusing an element (.focus()). => foucusing that element
// Selecting text (.select()).  => selecting that element
// Measuring the size of an element (width/height).
// Integrating with 3rd-party libraries (like Google Maps or D3.js).