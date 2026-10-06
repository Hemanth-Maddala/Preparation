# Tabs

## What is it?
Tabs show one section at a time. A single `activeTab` state value decides
which button is highlighted and which content renders.

## What this code demonstrates
Profile / Settings / Security tabs driven by one state value and an array
of tab definitions.

## Important code
- `const [activeTab, setActiveTab] = useState("profile")` — one value.
- `TABS.map(...)` with `className={activeTab === tab.id ? "active" : ""}` —
  highlight the active tab.
- `TABS.find((t) => t.id === activeTab).content` — show the right content.

## Interview questions
1. How do you switch tabs?
2. Why store the tab id, not a boolean per tab?
3. How would you add a count badge to a tab? (Derive it from data.)

## Common mistakes
- A separate boolean per tab (unscalable).
- Not highlighting the active tab.
- Storing the whole content object in state instead of just the id.

## Remember
- One state value = active tab id.
- Derive content and styling from it.
- Very common practical task — memorize it.
