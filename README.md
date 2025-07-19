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
docker run -p 8000:8000 --env-file .env atlantis-obfuscator
```

Visit `http://localhost:8000/docs` for Swagger UI.

### 2. Render Deployment

- Push this folder to GitHub
- Go to [render.com](https://render.com)
- Choose **New Web Service**
- Link GitHub repo and select:
  - **Runtime:** Docker
  - **Build Command:** leave empty
  - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- Add environment variable: `OPENAI_API_KEY`

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