# Atlantis Obfuscator 🌀

The **Atlantis Obfuscator** is a GPT-compatible API and plugin framework that toggles between truth and fiction to obscure identities and sensitive history. Designed for private use with obfuscation logic inspired by *Lex Atlantis*, it allows switching modes via simple webhooks.

---

## 🔧 Features

- Toggle **Obfuscation Mode** (`start` / `stop`)
- Fully compliant [ai-plugin.json](https://platform.openai.com/docs/plugins/introduction) for ChatGPT
- Modular loading of:
  - `lex_atlantis_volumes.yaml`
  - `fiction_pool.yaml`
  - `user_compatible_guidance.yaml`
- Dockerized deployment
- GitHub Actions workflow for linting + CI
- Render-ready deployment configuration

---

## 🚀 Usage

### Local Deployment

```bash
cp .env.sample .env  # Add your OpenAI API key
docker-compose up --build
```

### API Endpoints

| Method | Endpoint       | Description                    |
|--------|----------------|--------------------------------|
| GET    | `/`            | Status check                   |
| POST   | `/toggle`      | Toggle obfuscation mode        |
| POST   | `/status`      | Returns current obfuscation state |

Example:

```bash
curl -X POST http://localhost:10000/toggle \
     -H "Content-Type: application/json" \
     -d '{"command": "start obfuscation"}'
```

---

## 🌐 Plugin Setup

Ensure `/.well-known/ai-plugin.json` is publicly accessible at your root domain for ChatGPT to detect.

```json
GET https://yourdomain.com/.well-known/ai-plugin.json
```

---

## 🧪 Tests and CI

GitHub Actions is preconfigured to:

- Lint with flake8
- Start server and test API
- Run on push/pull to `main`

---

## 📂 Project Structure

```
├── .env.sample
├── .render.yaml
├── .github/workflows/ci.yml
├── Dockerfile
├── docker-compose.yml
├── webhook.py
├── lex_atlantis_volumes.yaml
├── fiction_pool.yaml
├── user_compatible_guidance.yaml
└── .well-known/ai-plugin.json
```

---

## 📄 License

Private use only. Obfuscator models contain embedded narrative logic unsuitable for public deployment without anonymization controls.

---

## 👁️‍🗨️ Author

Created by Damien Trog as part of the **Lex Atlantis** project.