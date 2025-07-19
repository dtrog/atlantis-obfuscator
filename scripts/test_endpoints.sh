#!/bin/bash

# Base URL - change to localhost or Docker internal network if needed
BASE_URL="http://localhost:10000"

echo "🔍 Testing Atlantis Obfuscator Endpoints..."

declare -a endpoints=(
  "/"
  "/health"
  "/docs"
  "/openapi.json"
  "/static/logo.png"
  "/.well-known/ai-plugin.json"
)

for endpoint in "${endpoints[@]}"
do
  echo -e "\n➡️ Testing: $BASE_URL$endpoint"
  curl -s -o /dev/null -w "📡 HTTP Status: %{http_code}\n" "$BASE_URL$endpoint"
done

echo -e "\n✅ Endpoint test complete."
