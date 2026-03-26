from pydantic import BaseModel


class LoginSchema(BaseModel):
    email: str
    password: str


class TicketCreate(BaseModel):
    title: str
    description: str
    user_id: int
    type: str