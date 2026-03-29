import { useEffect, useState } from "react";
import API from "../services/api";

export default function UserDashboard({ user }) {
  const [tickets, setTickets] = useState([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [aiResponse, setAiResponse] = useState(null);

  const fetchTickets = async () => {
    try {
      const res = await API.get("/tickets/my");
      setTickets(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  const createTicket = async () => {
    if (!title || !description) {
      alert("Enter title and description");
      return;
    }

    try {
      const res = await API.post("/tickets/create", {
        title,
        description,
      });

      setAiResponse(res.data);
      setTitle("");
      setDescription("");
      fetchTickets();
    } catch (err) {
      console.log(err.response?.data);
      alert("Error creating ticket");
    }
  };

  useEffect(() => {
    fetchTickets();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <div style={{ display: "flex", justifyContent: "space-between" }}>
        <h2>User Dashboard</h2>
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
        <input
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ display: "block", marginBottom: "10px", width: "300px" }}
        />

        <input
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          style={{ display: "block", marginBottom: "10px", width: "300px" }}
        />

        <button onClick={createTicket}>Create Ticket</button>
      </div>

      {aiResponse && (
        <div
          style={{
            border: "1px solid gray",
            marginTop: "20px",
            padding: "10px",
          }}
        >
          <h3>AI Response</h3>
          <p>
            <b>Category:</b> {aiResponse.category}
          </p>
          <p>
            <b>Response:</b> {aiResponse.response}
          </p>
          <p>
            <b>Ticket ID:</b> {aiResponse.ticket_number}
          </p>
        </div>
      )}

      <h3 style={{ marginTop: "30px" }}>My Tickets</h3>

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
        </div>
      ))}
    </div>
  );
}
