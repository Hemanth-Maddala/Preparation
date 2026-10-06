# Modal

## What is it?
A modal is an overlay on top of the page that appears/disappears based on
state. In React it is just conditional rendering + events + composition.

## What this code demonstrates
An `isOpen` boolean that shows or hides a modal, with close-on-overlay and
close-on-button.

## Important code
- `if (!isOpen) return null;` — render nothing when closed.
- `<div className="overlay" onClick={onClose}>` — click outside closes.
- `onClick={(e) => e.stopPropagation()}` — click inside does NOT close.

## Interview questions
1. How do you show/hide a modal in React?
2. Why `stopPropagation` on the modal box?
3. How would you close the modal with the Escape key? (useEffect + keydown.)

## Common mistakes
- Always rendering the modal and toggling CSS instead of conditional
  rendering.
- Not stopping propagation → clicking inside closes it.
- Putting the overlay style inline when a class is cleaner.

## Remember
- isOpen in state → conditional render.
- Overlay closes, inner box stops propagation.
- Escape key / focus trap are nice follow-ups in real apps.
