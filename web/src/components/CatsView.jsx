import React from "react";
import Section from "./Section";
import Heading from "./Heading";
import FoodCard from "./FoodCard";
import Cat from "./Cat";

const CatsView = () => {
  return (
    <Section id="features">
      <div className="container relative z-2">
        <Heading
          className="md:max-w-md lg:max-w-2xl text-center"
          title="Our Family"
        />
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10 ">
          {Array.from({ length: 6 }).map((_, i) => (
            <Cat
              name="Juan"
              image="https://images.squarespace-cdn.com/content/v1/59014ed8db29d637250fa476/1505638098078-XTTK0YX19ZR9QMVM6CRO/IMG_1040.JPG"
              desc="El es muy buena persona"
            />
          ))}
        </div>
      </div>
    </Section>
  );
};

export default CatsView;
