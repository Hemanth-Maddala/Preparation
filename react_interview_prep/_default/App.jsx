// Landing page for the interview-prep workspace.
// This copy is restored when you run: .\switch-example.ps1 _default

const CONCEPTS = [
  ["01_basic_component", "the smallest component"],
  ["02_jsx", "JSX expressions and fragments"],
  ["03_functional_components", "component composition"],
  ["04_props", "passing data into components"],
  ["05_children", "props.children"],
  ["06_useState", "state and re-rendering"],
  ["07_event_handling", "onClick, onChange, onSubmit"],
  ["08_conditional_rendering", "if / ternary / &&"],
  ["09_lists_and_keys", "map and keys"],
  ["10_forms", "a basic form"],
  ["11_controlled_components", "value + onChange"],
  ["12_form_validation", "validation with plain state"],
  ["13_login_page", "the classic interview task"],
  ["14_register_page", "registration form"],
  ["15_useEffect", "side effects and cleanup"],
  ["16_fetch_api", "fetch + useEffect"],
  ["17_loading_error_states", "loading/error/success"],
  ["18_useRef", "DOM refs and non-rendering values"],
  ["19_useContext", "theme context"],
  ["20_useReducer", "dispatch + reducer"],
  ["21_custom_hook", "useCounter"],
  ["22_local_storage", "persist across refresh"],
  ["23_react_router", "Routes, Route, Link"],
  ["24_navigation", "useNavigate"],
  ["25_protected_route", "auth redirect wrapper"],
  ["26_lifting_state", "shared state in the parent"],
  ["27_component_communication", "props + callbacks"],
  ["28_useMemo", "cache computed values"],
  ["29_useCallback", "stable function references"],
  ["30_memo", "prevent unnecessary renders"],
  ["31_debounce_search", "delay the search"],
  ["32_modal", "show/hide overlay"],
  ["33_tabs", "switch content"],
  ["34_search_filter", "filter a list"],
  ["35_pagination", "prev/next pages"],
  ["36_todo_crud", "add/delete/complete/edit"],
  ["37_api_crud", "GET/POST/PUT/DELETE"],
  ["38_auth_flow", "login + protect + logout"],
  ["39_error_boundary", "catch render errors"],
  ["40_practical_dashboard", "combine common patterns"],
  ["41_interview_tasks", "20 tasks with solutions"],
];

function App() {
  return (
    <div className="container">
      <h1>React Interview Prep</h1>
      <p>
        Load an example: <code>.\switch-example.ps1 06_useState</code> then{" "}
        <code>npm run dev</code>. Restore this page with{" "}
        <code>.\switch-example.ps1 _default</code>.
      </p>
      <ul>
        {CONCEPTS.map(([folder, desc]) => (
          <li key={folder}>
            <code>{folder}</code> — {desc}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
