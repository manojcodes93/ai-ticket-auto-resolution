import { useEffect, useState } from "react";
import API from "../services/api";

export default function AdminDashboard({ user }) {
  const [tickets, setTickets] = useState([]);
  const [filter, setFilter] = useState("all");

  const fetchTickets = async () => {
    try {
      let url = "/tickets";

      if (filter !== "all") {
        url += `?status=${filter}`;
      }

      const res = await API.get(url);
      setTickets(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    fetchTickets();
  }, [filter]);

  return (
    <div style={{ padding: "20px" }}>
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <h2>Admin Dashboard</h2>
        <button
          onClick={() => {
            localStorage.removeItem("token");
            window.location.reload();
          }}
        >
          Logout
        </button>
      </div>

      <div style={{ marginTop: "20px" }}>
        <button
          onClick={() => setFilter("all")}
          style={{ marginRight: "10px" }}
        >
          All
        </button>
        <button
          onClick={() => setFilter("resolved")}
          style={{ marginRight: "10px" }}
        >
          Closed
        </button>
        <button onClick={() => setFilter("open")}>Unresolved</button>
      </div>

      <div style={{ marginTop: "20px" }}>
        {tickets.map((t) => (
          <div
            key={t.ticket_number}
            style={{
              border: "1px solid gray",
              margin: "10px 0",
              padding: "10px",
            }}
          >
            <p>
              <b>{t.title}</b>
            </p>
            <p>Status: {t.status}</p>
            <p>Category: {t.category}</p>
            <p>Ticket No: {t.ticket_number}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
