// A wrapper component. It renders whatever JSX is placed between
// its tags by the parent — that content arrives as `children`.

function Card({ children }) {
  return <div className="card">{children}</div>;
}

export default Card;
