import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Section from "./Section"; // Asegúrate de que Section existe y está bien importado

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    if (username.trim() === "" || password.trim() === "") {
      alert("Por favor, ingresa un usuario y una contraseña");
      return;
    }

    const user = { name: username };
    localStorage.setItem("user", JSON.stringify(user));
    navigate("/");

    setTimeout(() => {
        window.location.reload();
    }, 100);
  };

  return (
    <Section>
      {/* From Uiverse.io by iZOXVL */}
      <div className="flex items-center justify-center h-screen">
      <div
        style={{ animation: "slideInFromLeft 1s ease-out" }}
        className="max-w-md w-full bg-gradient-to-r from-blue-800 to-purple-600 rounded-xl shadow-2xl overflow-hidden p-8 space-y-8"
      >
        <h2
          style={{ animation: "appear 2s ease-out" }}
          className="text-center text-4xl font-extrabold text-white"
        >
          Welcome
        </h2>
        <p style={{ animation: "appear 3s ease-out" }} className="text-center text-gray-200">
          Sign in to your account
        </p>

        <form onSubmit={handleLogin} className="space-y-6">
          <div className="relative">
            <input
              placeholder="john@example.com"
              className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-purple-500"
              required
              id="user"
              name="user"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <label
              className="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-purple-500 peer-focus:text-sm"
              htmlFor="user"
            >
              User
            </label>
          </div>

          <div className="relative">
            <input
              placeholder="Password"
              className="peer h-10 w-full border-b-2 border-gray-300 text-white bg-transparent placeholder-transparent focus:outline-none focus:border-purple-500"
              required
              id="password"
              name="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <label
              className="absolute left-0 -top-3.5 text-gray-500 text-sm transition-all peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400 peer-placeholder-shown:top-2 peer-focus:-top-3.5 peer-focus:text-purple-500 peer-focus:text-sm"
              htmlFor="password"
            >
              Password
            </label>
          </div>

          <button
            className="w-full py-2 px-4 bg-purple-500 hover:bg-purple-700 rounded-md shadow-lg text-white font-semibold transition duration-200"
            type="submit"
            onSubmit={handleLogin}
          >
            Sign In
          </button>
        </form>
      </div>
      </div>
    </Section>
  );
};

export default Login;