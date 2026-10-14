# """FastAPI application entry point."""
from app.models.user import User
from app.models.ticket import Ticket
from app.models.comment import Comment

from fastapi import FastAPI


from app.routes import auth, users,tickets


app = FastAPI(title="Service Desk API")

# Include each route module in the application.
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tickets.router)

app.get("/home")
def get_app():
    return {
        "message": "App is working"
    }