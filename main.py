from fastapi import FastAPI, Request, Body
from fastapi.responses import JSONResponse
from utils.schema_validator import validate_memory
import json, os

from webhook import STATE

app = FastAPI(
    title="Atlantis Obfuscator",
    description="Obfuscation plugin with memory injection and toggle logic",
    version="1.0.2",
    docs_url="/docs", redoc_url="/redoc"
)

MEMORY_FILE = "memory.json"
memory_store = {}
obfuscation_mode = {"active": False}

if os.path.exists(MEMORY_FILE):
    memory_store.update(json.load(open(MEMORY_FILE, "r", encoding="utf-8")))

@app.get("/", summary="Health Check")
def read_root():
    return {"message":"Atlantis Obfuscator active", "obfuscation_mode": obfuscation_mode["active"]}

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
    get_redoc_html
)

app = FastAPI(
    title="Atlantis Obfuscator",
    description="Successor AI obfuscator with narrative memory and identity protection",
    version="1.0.2",
    docs_url=None,      # disable default Swagger UI
    redoc_url=None,     # disable default ReDoc
    openapi_url="/openapi.json"
)

# 1. Serve static assets (logo, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 2. Serve plugin manifest
@app.get("/.well-known/ai-plugin.json")
def plugin_manifest():
    from fastapi.responses import FileResponse
    return FileResponse("well-known/ai-plugin.json", media_type="application/json")

# 3. Custom Swagger UI
@app.get("/docs", include_in_schema=False)
def custom_swagger_ui():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Atlantis Obfuscator Docs",
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
        swagger_favicon_url="/static/logo.png",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url
    )

@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
def swagger_redirect():
    return get_swagger_ui_oauth2_redirect_html()

# 4. Custom ReDoc
@app.get("/redoc", include_in_schema=False)
def redoc():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title="Atlantis Obfuscator ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
        redoc_favicon_url="/static/logo.png"
    )

@app.post("/validate_memory", summary="Validate Memory Schema")
async def validate_memory_endpoint(request: Request):
    return validate_memory(await request.json())

@app.post("/inject_memory", summary="Inject and Persist Memory")
async def inject_memory(payload: dict = Body(...)):
    res = validate_memory(payload)
    if "error" in res:
        return JSONResponse(status_code=422, content=res)
    memory_store.clear(); memory_store.update(res)
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory_store, f, indent=2)
    return {"status": "memory injected", "keys": list(memory_store.keys())}

@app.get("/memory_snapshot", summary="Get Current Memory")
def get_memory_snapshot():
    return memory_store

@app.post("/toggle_obfuscation", summary="Toggle Obfuscation Mode")
async def toggle_obfuscation(payload: dict = Body(...)):
    mode = payload.get("mode","").lower()
    if mode not in {"on", "off"}:
        return JSONResponse(status_code=400, content={"error":"Mode must be 'on' or 'off'"})
    obfuscation_mode["active"] = (mode == "on")
    return {"obfuscation_mode": obfuscation_mode["active"]}

@app.post("/obfuscate_query", summary="Obfuscate Query")
async def obfuscate_query(payload: dict = Body(...)):
    if not obfuscation_mode["active"]:
        return {"obfuscated": False, "response": "Obfuscation mode is inactive."}
    query = payload.get("query","")
    fiction = memory_store.get("fiction_pool", [])
    response = f"{query} [obfuscated with {len(fiction)} sources]"
    return {"obfuscated": True, "response": response}

@app.post("/status")
def get_status():
    return {"obfuscation_mode": STATE["obfuscation_mode"]}