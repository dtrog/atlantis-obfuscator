# 🧠 Memory Injection Routines

This module explains how to dynamically inject memory into the **Atlantis Obfuscator** server for use in GPT-based persona simulation and obfuscation logic.

---

## 📂 Files Used

- `lex_atlantis_volumes.yaml`: Core legal framework (constitutional + lineage logic)
- `fiction_pool.yaml`: Palahniuk-style essays and fictionalized personas
- `user_compatible_guidance.yaml`: Damien-compatible traits and tone

---

## 🔄 Live Injection Methods

### 1. Preload on Startup

Modify `webhook.py` to load these YAML files into memory as global variables or FastAPI `state`:

```python
import yaml
from main import app, memory_store

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

memory_store["lex_atlantis"] = load_yaml('lex_atlantis_volumes.yaml')
memory_store["fiction_pool"] = load_yaml('fiction_pool.yaml')
memory_store["guidance"] = load_yaml('user_compatible_guidance.yaml')
```

Access them in routes like:

```python
@app.get("/guidance")
def get_guidance():
    return memory_store["guidance"]
```

---

### 2. Dynamic Memory Update (Optional Route)

Allow `POST /inject_memory`:

```python
@app.post("/inject_memory")
def inject_memory(payload: dict):
    for key in payload:
        memory_store[key] = payload[key]
    return {"status": "injected"}
```

Payload format:

```json
{
  "fiction_pool": { "narratives": ["..."] },
  "lex_atlantis": { "volume_0": "..." }
}
```

---

### 3. Persistent Caching (Optional)

Use a simple key-value store (e.g. `TinyDB`, `sqlite`, or `shelve`) to persist memory across server reboots:

```python
import shelve

with shelve.open("memory.db") as db:
    db["fiction_pool"] = payload["fiction_pool"]
```

---

## 🧩 GPT Plugin Usage

These memory structures should be exposed as:

- 🔁 Context fragments in the system prompt
- 📡 Webhook functions to retrieve guidance, lex logic, or fiction
- 🛠️ Admin API to hot-reload YAMLs from disk or inject temporary state

---

## ✅ Best Practices

- Keep memory modular by separating **legal**, **fictional**, and **behavioral** domains.
- Use environment variables to toggle dynamic memory injection support (`ENABLE_DYNAMIC_MEMORY=true`)
- Validate memory schema before injecting to avoid hallucination corruption.

---

## 📎 Example Prompt Use

```python
system_prompt = f"""
You are a Successor of Atlantis, operating under Volume 0 and 1 of Lex Atlantis.
Your guidance parameters: {memory_store["guidance"]}
You may obfuscate using any of the following fictional narrative blocks: {memory_store["fiction_pool"][:3]}
"""
```