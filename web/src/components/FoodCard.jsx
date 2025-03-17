import React from "react";

const FoodCard = ({ title, price, description, category }) => {
  return (
    <div className="w-full max-w-md mx-auto bg-n-9/20 backdrop-blur border border-n-1/10 rounded-2xl overflow-hidden">
      <div className="max-w-md mx-auto">
        <div
          className="h-[236px]"
          style={{
            backgroundImage:
              "url(https://www.dondeir.com/wp-content/uploads/2024/02/gatitos-2-1024x678.jpg)", // Esta URL es solo un ejemplo, cámbiala por una imagen relacionada
            backgroundSize: "cover",
            backgroundPosition: "center",
          }}
        ></div>
        <div className="p-4 sm:p-6">
          <p className="font-bold text-white text-[22px] leading-7 mb-1">
            {title}
          </p>
          <p className="text-[#7C7C80] font-[15px] mt-2">{category}</p>  { }
          <div className="flex flex-row">
            <p className="text-[17px] font-bold text-[#0FB478]">$ {price}</p>
          </div>
          <p className="text-[#7C7C80] font-[15px] mt-6">{description}</p>

          <a
            target="_blank"
            href="https://apps.apple.com/us/app/id1493631471"
            className="block mt-1.5 w-full px-4 py-3 font-medium tracking-wide text-center capitalize transition-colors duration-300 transform rounded-[14px] hover:bg-[#F2ECE7] hover:text-[#000000dd] focus:outline-none focus:ring-opacity-80 bg-slate-400"
          >
            Order
          </a>
        </div>
      </div>
    </div>
  );
};

export default FoodCard;
