# Interview Tasks

The classic practical tasks with the exact format to plan before you code:
QUESTION, REQUIREMENTS, REACT CONCEPTS NEEDED, IMPLEMENTATION ORDER,
HINT, REFERENCE SOLUTION.

Method: read the QUESTION → try it from memory → check the HINT →
write it → compare with REFERENCE SOLUTION.

------------------------------------------------------------

## 1. Build a login page

QUESTION: "Build a login page with email, password, show/hide password,
validation, loading state, and a success message."

REQUIREMENTS: email + password inputs, show/hide toggle, inline errors,
disabled button while loading, success screen. Fake API, no backend.

REACT CONCEPTS NEEDED: useState, controlled inputs, event handling,
conditional rendering, async handler, basic validation.

IMPLEMENTATION ORDER:
1. State: email, password, showPassword, errors, loading, error, user.
2. Controlled inputs.
3. Show/hide toggle.
4. validate() on submit.
5. try/catch/finally around a fake login Promise.
6. Success branch + inline error rendering.

HINT: `if (user) return <h2>Welcome {user.name}</h2>;` before the form.
Demo login: `test@test.com` / `password`.

REFERENCE SOLUTION:

```jsx
import { useState } from "react";

const fakeLogin = (email, password) =>
  new Promise((resolve, reject) => {
    setTimeout(() => {
      if (email === "test@test.com" && password === "password")
        resolve({ token: "x", name: "Hemanth" });
      else reject(new Error("Invalid credentials"));
    }, 1000);
  });

function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [show, setShow] = useState(false);
  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [user, setUser] = useState(null);

  const validate = () => {
    const errs = {};
    if (!email) errs.email = "Email required";
    if (!password) errs.password = "Password required";
    return errs;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const errs = validate();
    setErrors(errs);
    if (Object.keys(errs).length) return;
    setLoading(true);
    setError("");
    try {
      setUser(await fakeLogin(email, password));
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  if (user) return <h2>Welcome, {user.name}!</h2>;

  return (
    <form onSubmit={handleSubmit} className="container">
      <input type="email" value={email}
        onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
      {errors.email && <p className="error">{errors.email}</p>}

      <input type={show ? "text" : "password"} value={password}
        onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
      <button type="button" onClick={() => setShow(!show)}>
        {show ? "Hide" : "Show"}
      </button>
      {errors.password && <p className="error">{errors.password}</p>}

      {error && <p className="error">{error}</p>}
      <button disabled={loading} type="submit">
        {loading ? "Logging in..." : "Login"}
      </button>
    </form>
  );
}

export default App;
```

------------------------------------------------------------

## 2. Build a signup page

QUESTION: "Build a signup page: name, email, password, confirm password."

REQUIREMENTS: validation for required fields, email format, password
length (min 6), and matching passwords. Success message.

REACT CONCEPTS NEEDED: one state object, controlled inputs, validation.

IMPLEMENTATION ORDER:
1. One `form` state object.
2. One `handleChange` using `[e.target.name]`.
3. `validate()` covering all four fields.
4. Gate submit + success branch.

HINT: compare `form.password !== form.confirmPassword`.

REFERENCE SOLUTION: see folder `14_register_page/App.jsx` (complete).

------------------------------------------------------------

## 3. Build a counter

QUESTION: "Build a counter with increment, decrement, and reset."

REQUIREMENTS: three buttons + a number. Disable decrement at 0.

REACT CONCEPTS NEEDED: useState, updater functions.

IMPLEMENTATION ORDER:
1. `const [count, setCount] = useState(0)`.
2. Three buttons calling the setter.
3. `disabled={count === 0}` on decrement.

HINT: use `setCount((c) => c + 1)` to be safe.

REFERENCE SOLUTION: see folder `06_useState/App.jsx` (complete).

------------------------------------------------------------

## 4. Build a todo list

QUESTION: "Build a todo list with add and delete."

REQUIREMENTS: input + Add, items with Delete. (Add complete + edit for
extra credit.)

REACT CONCEPTS NEEDED: useState, spread/filter, keys.

IMPLEMENTATION ORDER:
1. `todos` + `text` state.
2. Add: `setTodos([...todos, { id: Date.now(), text }])`.
3. Delete: `setTodos(todos.filter((t) => t.id !== id))`.
4. Render with `key={todo.id}`.

HINT: `id: Date.now()` for unique keys; guard empty input.

REFERENCE SOLUTION: see folder `36_todo_crud/App.jsx` (complete).

------------------------------------------------------------

## 5. Build a search filter

QUESTION: "Search through a list of items and show matching results."

REQUIREMENTS: input + filtered list + empty state.

REACT CONCEPTS NEEDED: controlled input, filter, conditional rendering.

IMPLEMENTATION ORDER:
1. `search` state.
2. `filtered = items.filter((i) => i.toLowerCase().includes(search.toLowerCase()))`.
3. Render filtered + "No results".

HINT: lowercase both sides.

REFERENCE SOLUTION: see folder `34_search_filter/App.jsx` (complete).

------------------------------------------------------------

## 6. Build tabs

QUESTION: "Build tabs: Profile, Settings, Security."

REQUIREMENTS: three buttons + one content area that swaps.

REACT CONCEPTS NEEDED: state, arrays, conditional rendering.

IMPLEMENTATION ORDER:
1. `activeTab` state.
2. Tabs array with id/label/content.
3. Map buttons; highlight active.
4. Show `TABS.find(...).content`.

HINT: store the id, not the content.

REFERENCE SOLUTION: see folder `33_tabs/App.jsx` (complete).

------------------------------------------------------------

## 7. Build a modal

QUESTION: "Build a modal that opens and closes."

REQUIREMENTS: Open button, overlay, close on outside click + button.

REACT CONCEPTS NEEDED: useState, conditional rendering, events.

IMPLEMENTATION ORDER:
1. `isOpen` state.
2. `if (!isOpen) return null;` in the Modal.
3. Overlay `onClick` closes; inner box `stopPropagation`.

HINT: `e.stopPropagation()` so clicking inside doesn't close.

REFERENCE SOLUTION: see folder `32_modal/App.jsx` (complete).

------------------------------------------------------------

## 8. Build pagination

QUESTION: "Paginate a list of 50 items, 5 per page."

REQUIREMENTS: Prev/Next buttons + page indicator + disabled edges.

REACT CONCEPTS NEEDED: useState, slice, math.

IMPLEMENTATION ORDER:
1. `page` state + `PAGE_SIZE`.
2. `pageItems = items.slice((page-1)*5, page*5)`.
3. Prev/Next with disabled guards.

HINT: `Math.ceil(items.length / PAGE_SIZE)`.

REFERENCE SOLUTION: see folder `35_pagination/App.jsx` (complete).

------------------------------------------------------------

## 9. Fetch and display API data

QUESTION: "Fetch posts from an API and display the titles."

REQUIREMENTS: loading state, list of titles, error handling.

REACT CONCEPTS NEEDED: useEffect, fetch, loading/error.

IMPLEMENTATION ORDER:
1. `posts`, `loading` state.
2. `useEffect` with `[]` → fetch → `.then(res => res.json())` → setPosts.
3. Early return while loading.

HINT: use jsonplaceholder. Empty deps = fetch once.

REFERENCE SOLUTION: see folders `16_fetch_api` and `17_loading_error_states`.

------------------------------------------------------------

## 10. Build a weather-style UI using mock data

QUESTION: "Build a weather card using mock data (city, temp, condition)."

REQUIREMENTS: a card showing mock weather, plus a button that "refreshes"
(mock loading), maybe a unit toggle.

REACT CONCEPTS NEEDED: useState, props, conditional rendering.

IMPLEMENTATION ORDER:
1. Mock weather object.
2. Card component via props.
3. `loading` + refresh button.
4. Toggle °C/°F.

HINT: `setLoading(true); setTimeout(() => setLoading(false), 800);`

REFERENCE SOLUTION:

```jsx
import { useState } from "react";

function WeatherCard({ city, temp, condition }) {
  return (
    <div className="card">
      <h2>{city}</h2>
      <p>{temp}°C — {condition}</p>
    </div>
  );
}

function App() {
  const [loading, setLoading] = useState(false);
  const [unit, setUnit] = useState("C");

  const refresh = () => {
    setLoading(true);
    setTimeout(() => setLoading(false), 800);
  };

  const temp = unit === "C" ? 24 : Math.round((24 * 9) / 5 + 32);

  return (
    <div className="container">
      {loading ? <p>Refreshing...</p> : (
        <WeatherCard city="Hyderabad" temp={temp} condition="Sunny" />
      )}
      <button onClick={refresh}>Refresh</button>
      <button onClick={() => setUnit(unit === "C" ? "F" : "C")}>
        Switch to °{unit === "C" ? "F" : "C"}
      </button>
    </div>
  );
}

export default App;
```

------------------------------------------------------------

## 11. Build a shopping cart

QUESTION: "Build a product list with add-to-cart and a total."

REQUIREMENTS: products, Add buttons, cart list, total price.

REACT CONCEPTS NEEDED: array updates, reduce, derived values.

IMPLEMENTATION ORDER:
1. `cart` state as array of `{ id, qty }`.
2. `add` — increment qty if present, else push.
3. `remove` — filter out.
4. `total = cart.reduce(...)`.

HINT: find the product price when computing the total.

REFERENCE SOLUTION: see REACT_CODING_TASKS.txt task 21 (complete).

------------------------------------------------------------

## 12. Build a product list with search

QUESTION: "Show products and filter them with a search box."

REQUIREMENTS: fetch or static products, search input, filtered render.

REACT CONCEPTS NEEDED: filter, controlled input, (optional fetch).

IMPLEMENTATION ORDER:
1. Products state (static or fetched).
2. Search state.
3. `filtered = products.filter(...)`.
4. Render filtered.

HINT: combine 05 and 09 patterns.

REFERENCE SOLUTION: see folder `34_search_filter` + `40_practical_dashboard`.

------------------------------------------------------------

## 13. Build a protected dashboard

QUESTION: "Make the dashboard accessible only after login."

REQUIREMENTS: login page, protected route, redirect when logged out.

REACT CONCEPTS NEEDED: React Router, Navigate, conditional rendering.

IMPLEMENTATION ORDER:
1. `isAuth` state (or Context/localStorage).
2. `ProtectedRoute` wrapper component.
3. Wrap the Dashboard route.
4. Login sets auth + navigates.

HINT: `isAuth ? children : <Navigate to="/login" replace />`.

REFERENCE SOLUTION: see folder `25_protected_route/App.jsx` (complete).

------------------------------------------------------------

## 14. Build a form with validation

QUESTION: "Validate email and password without any library."

REQUIREMENTS: errors shown inline, submit blocked when invalid.

REACT CONCEPTS NEEDED: controlled inputs, validate() pattern.

IMPLEMENTATION ORDER:
1. Fields state.
2. validate() returns errors object.
3. Render errors under fields.
4. Gate submit with `Object.keys(errs).length`.

HINT: `/^\S+@\S+\.\S+$/.test(email)`.

REFERENCE SOLUTION: see folder `12_form_validation/App.jsx` (complete).

------------------------------------------------------------

## 15. Build a debounced search

QUESTION: "Trigger a search 500ms after the user stops typing."

REQUIREMENTS: raw input + delayed action.

REACT CONCEPTS NEEDED: useEffect, setTimeout, cleanup.

IMPLEMENTATION ORDER:
1. `query` + `debounced` state.
2. Effect on `[query]`: timer → setDebounced; cleanup clears it.
3. Effect on `[debounced]`: run the search.

HINT: `return () => clearTimeout(timer);`.

REFERENCE SOLUTION: see folder `31_debounce_search/App.jsx` (complete).

------------------------------------------------------------

## 16. Build a dark/light theme

QUESTION: "Add a theme toggle that switches the whole page."

REQUIREMENTS: toggle button, classes change with theme.

REACT CONCEPTS NEEDED: useState (or Context for deep trees).

IMPLEMENTATION ORDER:
1. `theme` state.
2. Toggle handler.
3. `className={theme === "dark" ? "container dark" : "container"}`.

HINT: for multiple components use Context (folder 19).

REFERENCE SOLUTION: see folder `19_useContext/App.jsx` (complete).

------------------------------------------------------------

## 17. Build an expandable FAQ

QUESTION: "Click a question to expand its answer; one open at a time."

REQUIREMENTS: accordion behavior.

REACT CONCEPTS NEEDED: state (open index), conditional rendering, map.

IMPLEMENTATION ORDER:
1. FAQ array.
2. `openId` state.
3. Map items; render answer when `openId === i`.

HINT: store the index/id, not a boolean per item.

REFERENCE SOLUTION:

```jsx
import { useState } from "react";

const FAQ = [
  { q: "What is React?", a: "A UI library." },
  { q: "What is JSX?", a: "HTML-like syntax in JS." },
  { q: "What is a hook?", a: "Functions like useState." },
];

function App() {
  const [openId, setOpenId] = useState(0);
  return (
    <div className="container">
      {FAQ.map((item, i) => (
        <div key={item.q}>
          <button onClick={() => setOpenId(i)}>
            {item.q} {openId === i ? "▲" : "▼"}
          </button>
          {openId === i && <p>{item.a}</p>}
        </div>
      ))}
    </div>
  );
}

export default App;
```

------------------------------------------------------------

## 18. Build a dropdown

QUESTION: "Build a dropdown that opens, shows options, and fills the box."

REQUIREMENTS: button + list + click-to-select + close on outside click
(optional).

REACT CONCEPTS NEEDED: useState, conditional rendering, events.

IMPLEMENTATION ORDER:
1. `open` + `selected` state.
2. Button toggles open.
3. Options render when open; click sets selected + closes.

HINT: an `onBlur` or an overlay div closes on outside click.

REFERENCE SOLUTION:

```jsx
import { useState } from "react";

const OPTIONS = ["React", "Vue", "Angular", "Svelte"];

function App() {
  const [open, setOpen] = useState(false);
  const [selected, setSelected] = useState("Choose a framework");

  return (
    <div className="container" style={{ position: "relative" }}>
      <button onClick={() => setOpen(!open)}>{selected}</button>
      {open && (
        <ul className="card" style={{ listStyle: "none", margin: 0 }}>
          {OPTIONS.map((o) => (
            <li key={o}>
              <button
                onClick={() => {
                  setSelected(o);
                  setOpen(false);
                }}
              >
                {o}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
```

------------------------------------------------------------

## 19. Build a star rating

QUESTION: "Click stars to set a rating from 1 to 5."

REQUIREMENTS: 5 stars, filled up to the chosen rating.

REACT CONCEPTS NEEDED: arrays, index state, inline styles.

IMPLEMENTATION ORDER:
1. `rating` state.
2. Render [1..5].map → ★ button.
3. `n <= rating` → filled color.

HINT: add `onMouseEnter` for hover feel.

REFERENCE SOLUTION: see REACT_CODING_TASKS.txt task 33 (complete).

------------------------------------------------------------

## 20. Build an autocomplete input

QUESTION: "Show matching suggestions as the user types; clicking fills the input."

REQUIREMENTS: input + suggestion list + click-to-fill.

REACT CONCEPTS NEEDED: filter, conditional rendering, events.

IMPLEMENTATION ORDER:
1. `q` + `selected` state.
2. `matches = list.filter(...includes(q))`.
3. Show list when `q !== selected`; click fills both.

HINT: only show suggestions when there is something to suggest.

REFERENCE SOLUTION: see REACT_CODING_TASKS.txt task 32 (complete).
