import React from "react";
import { companyLogos } from "../constants";

const CompanyLogos = ({ className }) => {
  return (
    <div className={className}>
      <h5 className="tagline mb-6 text-center text-n-1/50">
        Preparamos tus alimentos con la más alta tecnología y claro, con la mejor compañia.
      </h5>
    </div>
  );
};

export default CompanyLogos;
