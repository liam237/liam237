import json
import random
from datetime import datetime

# Chemin vers le fichier README
readme_path = "README.md"
# Chemin vers le fichier JSON contenant les fun facts
fun_facts_path = "assets/fun_facts.json"

# Charger les fun facts
with open(fun_facts_path, "r", encoding="utf-8") as f:
    fun_facts = json.load(f)

# Choisir un fun fact selon le mois
current_month = datetime.now().month
fun_fact = fun_facts[(current_month - 1) % len(fun_facts)]

# Créer le bloc markdown à insérer
new_block = f"""### 🤯 Fun Fact  
🧠 Did you know? {fun_fact['question']}  
<details>
    <summary>Click to reveal the answer</summary>
  🔍 **A:** {fun_fact['answer']}
</details>"""

# Lire le README
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remplacer l'ancien bloc Fun Fact (entre les délimiteurs "---\n### 🤯 Fun Fact" et la ligne suivante "---")
import re
pattern = r"### 🤯 Fun Fact[\s\S]*?<details>[\s\S]*?</details>"
updated_content = re.sub(pattern, new_block, content)

# Écrire les modifications
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(updated_content)

print("✅ Fun Fact successfully updated!")