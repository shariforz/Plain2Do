import { createContext, useEffect, useState } from "react";

export const AuthContext = createContext();

export const AuthContextProvider = ({ children }) => {
  const initialToken = JSON.parse(localStorage.getItem("access"));
  const [token, setToken] = useState(initialToken);

  useEffect(() => {
    if (token) {
      return localStorage.setItem("access", JSON.stringify(token));
    }

    localStorage.removeItem("access");
  });

  return (
    <AuthContext.Provider value={{ token, setToken }}>
      {children}
    </AuthContext.Provider>
  );
};
