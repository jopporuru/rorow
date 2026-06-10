from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

latest_command = "S"

@app.get("/")
def home():
    return{"status": "shits on"}

@app.get("/command")
def get_command():
    global latest_command
    cmd = latest_command
    latest_command = "S"
    return {"command": cmd}

@app.get("/command/{cmd}")
def set_command(cmd: str):
    global latest_command
    latest_command = cmd.upper()
    return {"status": "oks", "command": latest_command}
