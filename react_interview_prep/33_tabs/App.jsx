// Tabs: one `activeTab` state drives which content is shown.

import { useState } from "react";

const TABS = [
  { id: "profile", label: "Profile", content: "Your profile details go here." },
  { id: "settings", label: "Settings", content: "Settings content goes here." },
  { id: "security", label: "Security", content: "Security content goes here." },
];

function App() {
  const [activeTab, setActiveTab] = useState("profile");

  // Find the active tab's content
  const activeContent = TABS.find((tab) => tab.id === activeTab).content;

  return (
    <div className="container">
      <h1>Tabs</h1>

      <div className="tabs">
        {TABS.map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={activeTab === tab.id ? "tab active" : "tab"}
          >
            {tab.label}
          </button>
        ))}
      </div>

      <div className="card">{activeContent}</div>
    </div>
  );
}

export default App;
