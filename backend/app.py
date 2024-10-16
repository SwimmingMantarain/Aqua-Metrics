from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import auth, users
from .database import Base, engine

# Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS (important for frontend to communicate with API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router, prefix="/api/auth")
app.include_router(users.router, prefix="/api/users")

@app.get("/")
def read_root():
    return {"message": "Welcome to Aqua-Metrics API!"}
