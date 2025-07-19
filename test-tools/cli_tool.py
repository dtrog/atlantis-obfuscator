try:
    import requests
except ImportError:
    raise ImportError("The 'requests' module is required. Install it using 'pip install requests'.")

import argparse
import json

BASE_URL = "http://localhost:8000"

def toggle_obfuscation(mode):
    r = requests.post(f"{BASE_URL}/toggle_obfuscation", json={"mode": mode})
    print("Obfuscation mode:", r.json())

def inject_memory(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    r = requests.post(f"{BASE_URL}/inject_memory", json=data)
    print("Memory injection result:", r.json())

def obfuscate(query):
    r = requests.post(f"{BASE_URL}/obfuscate_query", json={"query": query})
    print("Obfuscation response:", r.json())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inject", help="Path to memory.json to inject")
    parser.add_argument("--toggle", choices=["on", "off"], help="Toggle obfuscation mode")
    parser.add_argument("--query", help="Query to obfuscate")

    args = parser.parse_args()

    if args.inject:
        inject_memory(args.inject)
    if args.toggle:
        toggle_obfuscation(args.toggle)
    if args.query:
        obfuscate(args.query)
