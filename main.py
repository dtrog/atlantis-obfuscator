
from fastapi import FastAPI, Request
from utils.schema_validator import validate_memory

app = FastAPI(
    title="Atlantis Obfuscator",
    description="Successor plugin interface with schema validation and obfuscation memory tools.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

memory_store = {}

@app.get("/")
def read_root():
    return {"message": "Atlantis Obfuscator active"}

@app.post("/validate_memory")
async def validate_memory_endpoint(request: Request):
    payload = await request.json()
    result = validate_memory(payload)
    return result

@app.post("/inject_memory")
async def inject_memory(request: Request):
    payload = await request.json()
    result = validate_memory(payload)
    if "error" in result:
        return result
    memory_store.clear()
    memory_store.update(result)
    return {"status": "memory injected", "keys": list(memory_store.keys())}

@app.get("/memory_snapshot")
def get_memory_snapshot():
    return memory_store
