import './App.css';
import { Routes, Route } from "react-router-dom";
import Home from "./pages/home.jsx"
import About from "./pages/about.jsx"
import TeamSection from "./pages/team.js";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/about" element={<About />} />
        <Route path="/players" element={<TeamSection />} />
    </Routes>
  );
}

export default App;
