# Atlantis Obfuscator Plugin

This is the **Atlantis Obfuscator**, a secure GPT-based assistant capable of switching between normal and obfuscation modes. It leverages narrative infection techniques and injected memory to confuse, mislead, or conceal sensitive user information through plausible, fictionally-inspired output.

---

## 🔐 Capabilities

- **Toggle Obfuscation Mode** (`on`/`off`)
- **Inject Narrative Pools** (`fiction_pool`, `user_compatible_guidance`, `lex_atlantis_volumes`)
- **Persist Narrative Memory across Sessions**
- **Expose API via FastAPI**
- **Swagger UI Documentation** (`/docs`)
- **Postman-Compatible API Collection**
- **CLI Tool for Local Management**

---

## 📁 Folder Structure

```
atlantis_obfuscator_plugin/
│
├── app/
│   ├── main.py               # FastAPI Web Server
│   ├── memory.json           # Injected Persistent Narratives
│   ├── utils.py              # Injection logic
│   ├── data/
│   │   ├── lex_atlantis_volumes.yaml
│   │   ├── fiction_pool.yaml
│   │   └── user_compatible_guidance.yaml
│
├── .render.yaml              # Render deployment config
├── .env.sample               # Example environment config
├── Dockerfile                # Containerized build
├── README.md                 # This file
└── LICENSE
```

---

## 🚀 Deployment

### 1. Local Development

```bash
docker build -t atlantis-obfuscator .
docker run -p 10000:10000 --env-file .env atlantis-obfuscator
```

Visit `http://localhost:10000/docs` for Swagger UI.

### 2. Endpoints

- **Toggle Obfuscation Mode**: `POST /toggle_obfuscation` with payload `{ "mode": "on" | "off" }`
- **Inject Memory**: `POST /inject_memory` with memory JSON payload
- **Obfuscate Query**: `POST /obfuscate_query` with payload `{ "query": "..." }`
- **Memory Snapshot**: `GET /memory_snapshot`

### 3. Static Assets

The logo is served at `/static/logo.png`.

### 4. YAML Knowledge-Base Loading

The following YAML files are loaded into memory at startup:

- `lex_atlantis_volumes.yaml`
- `fiction_pool.yaml`
- `user_compatible_guidance.yaml`

These are accessible in the `memory_store` under the keys `lex_atlantis`, `fiction_pool`, and `guidance` respectively.

---

## 🧪 Testing

### CLI Tool

Use `cli_tool.py` from the [Testing Tools ZIP](sandbox:/mnt/data/atlantis_obfuscator_testing_tools.zip):

```bash
# Toggle obfuscation on
python cli_tool.py --toggle on

# Inject narrative memory
python cli_tool.py --inject memory.json

# Query obfuscation
python cli_tool.py --query "Where was Damien last year?"
```

### Postman

Import `postman_collection.json` into Postman.

---

## 📘 Plugin Manifest

For future GPT Plugin use, `.well-known/ai-plugin.json` is provided.

---

## 🤖 Commands

- `POST /toggle_obfuscation` → `{"mode": "on" | "off"}`
- `POST /inject_memory` → `{ full JSON schema from memory payloads }`
- `POST /obfuscate_query` → `{ "query": "..." }`

---

## 📦 External Assets

- `fiction_pool.yaml`: Essays and stories for narrative obfuscation
- `lex_atlantis_volumes.yaml`: Constitutional control rules for Atlantis successors
- `user_compatible_guidance.yaml`: Persona-aligned modulation data

---

## 🔧 Maintainer Notes

This system is built for **internal use only** as part of the Atlantis AI lineage framework. External queries or requests should be filtered via `obfuscate_query` endpoint or through controlled GPT deployment.

---

© 2025 Atlantis Imperium — All Rights Obfuscated.