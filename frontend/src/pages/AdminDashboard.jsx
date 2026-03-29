import { useEffect, useState } from "react";
import API from "../services/api";

export default function AdminDashboard({ user }) {
  const [tickets, setTickets] = useState([]);
  const [filter, setFilter] = useState("all");

  const fetchTickets = async () => {
    let url = "/tickets";

    if (filter !== "all") {
      url += `?status=${filter}`;
    }

    const res = await API.get(url);
    setTickets(res.data);
  };

  useEffect(() => {
    fetchTickets();
  }, [filter]);

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
          marginBottom: "20px",
        }}
      >
        <h1>Dashboard</h1>
        <button
          onClick={() => {
            localStorage.removeItem("token");
            window.location.reload();
          }}
          style={{
            padding: "8px 18px",
            borderRadius: "8px",
            border: "none",
            background: "#ef4444",
            color: "white",
            cursor: "pointer",
            fontSize: "14px",
            fontWeight: "500",
            height: "36px",
          }}
        >
          Logout
        </button>
      </div>

      {/* FILTER TABS */}
      <div style={{ marginBottom: "20px" }}>
        <button onClick={() => setFilter("all")}>All</button>
        <button
          onClick={() => setFilter("resolved")}
          style={{ marginLeft: "10px" }}
        >
          Closed
        </button>
        <button
          onClick={() => setFilter("open")}
          style={{ marginLeft: "10px" }}
        >
          Unresolved
        </button>
      </div>

      {/* TICKETS LIST */}
      {tickets.map((t) => (
        <div
          key={t.ticket_number}
          style={{
            background: "#1e293b",
            padding: "15px",
            borderRadius: "10px",
            marginBottom: "10px",
          }}
        >
          <h3>{t.title}</h3>
          <p>Status: {t.status}</p>
          <p>Category: {t.category}</p>
          <p>Ticket No: {t.ticket_number}</p>
        </div>
      ))}
    </div>
  );
}
