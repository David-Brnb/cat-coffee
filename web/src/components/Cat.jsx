import React from "react";

const Cat = ({ name, image, desc }) => {
  return (
    <div class="card">
      <img src={image} width="400px" />
      <div class="card__content">
        <p class="card__title">{name}</p>
        <p class="card__description">{desc}</p>
      </div>
    </div>
  );
};

export default Cat;
