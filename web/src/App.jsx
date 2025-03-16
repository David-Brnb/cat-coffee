import ButtonGradient from "./assets/svg/ButtonGradient";
import Benefits from "./components/Benefits";
import Menu from "./components/Menu";
import Header from "./components/Header";
import Hero from "./components/Hero";
import CatsView from "./components/CatsView";

const App = () => {
  return (
    <>
      <div className="pt-[4.75rem] lg:pt-[5.25rem] overflow-hidden">
        <Header />
        <Hero />
        <Menu />
        <CatsView />
      </div>
      <ButtonGradient />
    </>
  );
};

export default App;
