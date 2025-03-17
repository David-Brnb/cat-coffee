import React, { useEffect, useState } from "react";
import Section from "./Section";
import Heading from "./Heading";
import FoodCard from "./FoodCard";
import Cat from "./Cat";

const Menu = () => {
  const [menuItems, setMenuItems] = useState([]);
  const [loading, setLoading] = useState(true);  

  useEffect(() => {

    fetch("http://127.0.0.1:8000/menu")  
      .then((response) => response.json())
      .then((data) => {
        setMenuItems(data);  
        setLoading(false);    
      })
      .catch((error) => {
        console.error("Error al obtener el menú:", error);
        setLoading(false);   
      });
  }, []);

  if (loading) {
    return <div>Cargando...</div>; 
  }

  return (
    <Section id="features">
      <div className="container relative z-2">
        <Heading
          className="md:max-w-md lg:max-w-2xl text-center"
          title="Some of Our Food"
        />
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10">
          {menuItems.length > 0 ? (
            menuItems.map((item) => (
              <FoodCard
                key={item.id}
                title={item.nombre} 
                price={item.precio} 
                description={item.descripcion}  
                category={item.categoria} 
              />
            ))
          ) : (
            <div>No se encontraron platillos.</div>
          )}
        </div>
      </div>
    </Section>
  );
};

export default Menu;
