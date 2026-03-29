import { useState } from "react";
import API from "../services/api";

export default function Login({ setUser }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    if (!username || !password) {
      alert("Enter email and password");
      return;
    }

    try {
      const res = await API.post("/login", {
        username,
        password,
      });

      console.log("LOGIN RESPONSE:", res.data);

      localStorage.setItem("token", res.data.access_token);
      setUser(res.data.user);
    } catch (err) {
      console.log("ERROR:", err.response?.data);
      alert("Login failed");
    }
  };

  return (
    <div
      style={{
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background: "#0f172a",
      }}
    >
      <div
        style={{
          background: "#1e293b",
          padding: "30px",
          borderRadius: "12px",
          width: "320px",
          textAlign: "center",
          color: "white",
        }}
      >
        <h2 style={{ marginBottom: "20px" }}>AI Ticket System</h2>

        <input
          placeholder="Enter email"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={{
            width: "100%",
            padding: "12px",
            margin: "10px 0",
            borderRadius: "8px",
            border: "none",
            outline: "none",
            boxSizing: "border-box",
          }}
        />

        <input
          type="password"
          placeholder="Enter password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={{
            width: "100%",
            padding: "12px",
            margin: "10px 0",
            borderRadius: "8px",
            border: "none",
            outline: "none",
            boxSizing: "border-box",
          }}
        />

        <button
          onClick={handleLogin}
          style={{
            width: "100%",
            padding: "12px",
            marginTop: "10px",
            borderRadius: "8px",
            border: "none",
            background: "#3b82f6",
            color: "white",
            cursor: "pointer",
            boxSizing: "border-box",
          }}
        >
          Login
        </button>
      </div>
    </div>
  );
}
