import React from "react";

const Cat = ({ name, image, desc }) => {
  return (
    <div class="card">
      <img 
        src={image} 
        style={{ width: "100%", height: "100%", objectFit: "cover" }} 
      />

      <div class="card__content">
        <p class="card__title">{name}</p>
        <p class="card__description">{desc}</p>
      </div>
    </div>
  );
};

export default Cat;
