from fastapi import FastAPI, Request
from pydantic import BaseModel
import os

app = FastAPI()

class ObfuscationCommand(BaseModel):
    command: str

STATE = {"obfuscation_mode": False}

@app.get("/")
def read_root():
    return {
        "message": "Atlantis Obfuscator active",
        "obfuscation_mode": STATE["obfuscation_mode"]
    }

@app.post("/toggle")
def toggle_obfuscation(cmd: ObfuscationCommand):
    if cmd.command.lower() == "start obfuscation":
        STATE["obfuscation_mode"] = True
        return {"status": "obfuscation mode enabled"}
    elif cmd.command.lower() == "stop obfuscation":
        STATE["obfuscation_mode"] = False
        return {"status": "obfuscation mode disabled"}
    else:
        return {"status": "unknown command"}

@app.post("/status")
def get_status():
    return {"obfuscation_mode": STATE["obfuscation_mode"]}