import { Routes, Route } from "react-router-dom";
import ButtonGradient from "./assets/svg/ButtonGradient";
import Header from "./components/Header";
import Hero from "./components/Hero";
import Menu from "./components/Menu";
import CatsView from "./components/CatsView";
import Login from "./components/Login";

const App = () => {
  return (
    <>
      <Header />
      <div className="pt-[4.75rem] lg:pt-[5.25rem] overflow-hidden">
        <Routes>
          <Route path="/menu" element={<Menu />} />
          <Route path="/cats" element={<CatsView />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
      <ButtonGradient />
    </>
  );
};

export default App;
