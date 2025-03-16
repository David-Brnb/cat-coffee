import React from "react";
import Section from "./Section";
import Heading from "./Heading";
import FoodCard from "./FoodCard";
import Cat from "./Cat";

const Menu = () => {
  return (
    <Section id="features">
      <div className="container relative z-2">
        <Heading
          className="md:max-w-md lg:max-w-2xl text-center"
          title="Some of Our Food"
        />
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 ">
          {Array.from({ length: 8 }).map((_, i) => (
            <FoodCard
              key={i}
              title={`Titulo ${i + 1}`}
              price={500 + i * 10}
              description="Another delicious dish with amazing flavors."
            />
          ))}
        </div>
      </div>
    </Section>
  );
};

export default Menu;
