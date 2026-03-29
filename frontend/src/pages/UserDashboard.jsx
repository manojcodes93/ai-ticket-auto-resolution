import { useEffect, useState } from "react";
import API from "../services/api";

export default function UserDashboard({ user }) {
  const [tickets, setTickets] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [aiResponse, setAiResponse] = useState(null);

  const fetchTickets = async () => {
    const res = await API.get("/tickets/my");
    setTickets(res.data);
  };

  const createTicket = async () => {
    const res = await API.post("/tickets/create", { title, description });
    setAiResponse(res.data);
    setTitle("");
    setDescription("");
    fetchTickets();
  };

  useEffect(() => {
    fetchTickets();
  }, []);

  return (
    <div
      style={{
        padding: "30px",
        background: "#0f172a",
        minHeight: "100vh",
        color: "white",
      }}
    >
      {/* HEADER */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <h1>Dashboard</h1>

        {/* POWER BUTTON */}
        <button
          onClick={() => {
            localStorage.removeItem("token");
            window.location.reload();
          }}
          style={{
            padding: "8px 16px",
            borderRadius: "8px",
            border: "none",
            background: "#ef4444",
            color: "white",
            cursor: "pointer",
            fontWeight: "500",
          }}
        >
          Logout
        </button>
      </div>

      {/* FORM */}
      <div
        style={{
          background: "#1e293b",
          padding: "20px",
          borderRadius: "12px",
          marginTop: "20px",
        }}
      >
        <h2
          style={{
            textAlign: "center",
            marginBottom: "15px",
            fontSize: "22px",
          }}
        >
          Create Ticket
        </h2>

        {/* SAME LEFT ALIGN CONTAINER */}
        <div style={{ width: "80%", margin: "0 auto", textAlign: "left" }}>
          <input
            placeholder="Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            style={{
              width: "100%",
              padding: "10px",
              margin: "10px 0",
              borderRadius: "8px",
              border: "none",
            }}
          />

          <textarea
            placeholder="Description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            style={{
              width: "100%",
              padding: "10px",
              margin: "10px 0",
              borderRadius: "8px",
              border: "none",
            }}
          />

          {/* BUTTON RIGHT SIDE */}
          <div style={{ textAlign: "right" }}>
            <button
              onClick={createTicket}
              style={{
                padding: "10px 20px",
                borderRadius: "8px",
                border: "none",
                background: "#22c55e",
                color: "white",
                cursor: "pointer",
              }}
            >
              Submit
            </button>
          </div>
        </div>
      </div>
      {/* AI RESPONSE */}
      {aiResponse && (
        <div
          style={{
            background: "#1e293b",
            padding: "20px",
            borderRadius: "12px",
            marginTop: "20px",
          }}
        >
          <h2>AI Response</h2>

          <p>
            <b>Ticket No:</b> {aiResponse.ticket_number}
          </p>
          <p>
            <b>Response:</b> {aiResponse.response}
          </p>
          <p>
            <b>Category:</b> {aiResponse.category}
          </p>
        </div>
      )}

      {/* TICKETS */}
      <h2 style={{ marginTop: "30px" }}>My Tickets</h2>

      {tickets.map((t) => (
        <div
          key={t.ticket_number}
          style={{
            background: "#1e293b",
            padding: "15px",
            borderRadius: "10px",
            marginTop: "10px",
          }}
        >
          <h3>{t.title}</h3>
          <p>Status: {t.status}</p>
        </div>
      ))}
    </div>
  );
}
