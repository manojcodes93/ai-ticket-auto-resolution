from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Ticket
from backend.schemas import TicketCreate
from model.ai_engine import solve_ticket
from datetime import datetime

router = APIRouter()



def generate_ticket_number(db: Session):

    year = datetime.now().year

    # Count existing tickets
    count = db.query(Ticket).count() + 1

    return f"TICK-{year}-{str(count).zfill(4)}"


@router.post("/tickets")
def create_ticket(data: TicketCreate, db: Session = Depends(get_db)):

    # Generate ticket number
    ticket_number = generate_ticket_number(db)

    # AI response
    result = solve_ticket(data.description)

    confidence = result.get("Confidence Score", 0)
    status = "CLOSED" if confidence > 60 else "ACTION_REQUIRED"

    ticket = Ticket(
        ticket_number=ticket_number,   # ✅ NEW
        title=data.title,
        description=data.description,
        response=result.get("response", ""),
        category=result.get("category", "Unknown"),
        status=status,
        user_id=data.user_id,
        type=data.type
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return {
        "ticket_number": ticket.ticket_number,
        "title": ticket.title,
        "status": ticket.status,
        "response": ticket.response
    }