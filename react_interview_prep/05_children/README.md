# Children

## What is it?
`children` is a special prop. Whatever you place between a component's
opening and closing tags is passed to it automatically as `props.children`.
It lets you build wrappers/layout components.

## What this code demonstrates
A `Card` wrapper that provides the styling and layout, while the parent
supplies the actual content via children.

## Important code
- `<Card> ...content... </Card>` — content is collected as children.
- `function Card({ children })` — Card receives children as a prop.
- `{children}` inside the JSX — where the content is rendered.

## Interview questions
1. What is `props.children`?
2. When is children useful?
3. How do you build a reusable wrapper/layout component?

## Common mistakes
- Forgetting to render `{children}` — the content silently disappears.
- Passing children but also wanting props — both work fine together.

## Remember
- Children = content between tags.
- Great for `Card`, `Modal`, `Layout`, `Button`-style wrappers.
- Always render `{children}` in the wrapper, or nothing shows.
