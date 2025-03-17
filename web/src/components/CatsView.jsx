import React, { useState, useEffect } from "react"; 
import Heading from "./Heading";
import Section from "./Section"; 
import Cat from "./Cat";

const CatsView = () => {
  const [cats, setCats] = useState([]); 
  const [loading, setLoading] = useState(true); 

  useEffect(() => {
    fetch("http://127.0.0.1:8000/gatos")
      .then((response) => response.json())
      .then((data) => {
        const catsWithImages = data.map((cat) => {
          return fetch(`http://127.0.0.1:8000/imagen_gato/${cat.id}`)
            .then((res) => res.json())
            .then((imageData) => ({
              ...cat,
              imageUrl: `http://127.0.0.1:8000/${imageData.ruta_foto}`,
            }))
            .catch((error) => {
              console.error("Error al obtener la imagen:", error);
              return { ...cat, imageUrl: null };
            });
        });
        Promise.all(catsWithImages).then((catsWithImagesData) => {
          setCats(catsWithImagesData);
          setLoading(false); 
        });
      })
      .catch((error) => {
        console.error("Error", error);
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
          title="Our Family"
        />
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10">
          {cats.length > 0 ? (
            cats.map((cat) => (
              <Cat
                key={cat.id}
                name={cat.nombre}
                desc={cat.descripcion}
                image={cat.imageUrl} 
              />
            ))
          ) : (
            <div>No se encontraron gatos.</div> 
          )}
        </div>
      </div>
    </Section>
  );
};

export default CatsView;
