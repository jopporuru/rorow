from fastapi import FastAPI

app = FastAPI()

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
