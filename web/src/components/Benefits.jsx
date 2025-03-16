import React from "react";
import Section from "./Section";
import Heading from "./Heading";
import { benefits } from "../constants";

import card1 from "../assets/benefits/card-1.svg";

const Benefits = () => {
  return (
    <Section id="features">
      <div className="container relative z-2">
        <Heading
          className="md:max-w-md lg:max-w-2xl"
          title="Chat Smarter, Not Harder with Brainwave"
        />
        <div className="flex flex-wrap gap-10 mb-10">
          {benefits.map((item) => {
            console.log(item.backgroundUrl);
            return (
              <div
                className="block relative p-0.5 bg-no-repeat bg-[length:100%_100%] md:max-w-[24rem]"
                style={{
                  backgroundImage: `url(${card1})`,
                }}
                key={item.id}
              >
                <div>
                  <h5>{item.title}</h5>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </Section>
  );
};

export default Benefits;
