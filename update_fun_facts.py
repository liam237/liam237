import json
from datetime import datetime

# Load fun facts from assets folder
with open("assets/fun_facts.json", "r", encoding="utf-8") as f:
    fun_facts = json.load(f)

# Select fun fact based on the current month
current_month = datetime.now().month - 1
fun_fact = fun_facts[current_month]

# Read the README
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find and replace Fun Fact block
start_tag = "### 🤯 Fun Fact"
start_idx = None
for i, line in enumerate(lines):
    if start_tag in line:
        start_idx = i
        break

if start_idx is not None:
    end_idx = start_idx + 5  # assume Fun Fact block has 5 lines
    lines[start_idx:end_idx] = [
        "### 🤯 Fun Fact\n",
        f"🧠 Did you know? {fun_fact}\n"
    ]

# Write back to README
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(lines)