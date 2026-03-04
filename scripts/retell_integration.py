import json
import os

PROMPT_PATH = "outputs/accounts/ben_electric_001/v1/agent_prompt.txt"

with open(PROMPT_PATH, "r") as f:
    prompt = f.read()

print("Prompt ready for Retell deployment:")
print(prompt)