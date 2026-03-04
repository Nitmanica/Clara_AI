import os
import json

# ---------- READ TRANSCRIPT ----------
transcript_path = "data/demo_calls/ben_electric_demo.txt"

with open(transcript_path, "r", encoding="utf-8") as f:
    transcript = f.read()


# ---------- SIMPLE EXTRACTION ----------
company_name = "Ben's Electric Solutions"
crm_system = "Jobber"

services_supported = [
    "EV charger installation",
    "panel changes",
    "electrical troubleshooting",
    "outlet replacement",
    "hot tub hookup",
    "renovation electrical work"
]


# ---------- ACCOUNT MEMO ----------
memo = {
    "account_id": "ben_electric_001",
    "company_name": company_name,
    "services_supported": services_supported,
    "crm_system": crm_system,
    "emergency_definition": [
        "electrical sparks",
        "power failure"
    ],
    "questions_or_unknowns": [
        "business hours not specified",
        "timezone not specified"
    ],
    "notes": "Owner currently answers most calls himself"
}


# ---------- AGENT SPEC ----------
agent_spec = {
    "agent_name": "Ben Electric AI Receptionist",
    "voice_style": "friendly professional",
    "version": "v1",
    "key_variables": {
        "company_name": company_name,
        "crm_system": crm_system
    }
}


# ---------- AGENT PROMPT ----------
agent_prompt = """
You are Clara, the AI receptionist for Ben's Electric Solutions.

BUSINESS HOURS FLOW
1. Greet the caller.
2. Ask the purpose of the call.
3. Collect name and phone number.
4. Determine if the issue is emergency or non-emergency.
5. If emergency, transfer the call to the owner.
6. If non-emergency, collect job details and inform the customer someone will follow up.
7. Ask if they need anything else.
8. End the call politely.

AFTER HOURS FLOW
1. Greet the caller.
2. Ask the reason for the call.
3. Confirm if it is an emergency.
4. If emergency collect name, phone number, and address.
5. Attempt transfer.
6. If transfer fails apologize and assure follow-up.
7. If non-emergency collect details and confirm follow-up during business hours.
"""


# ---------- CREATE OUTPUT FOLDER ----------
output_dir = "outputs/accounts/ben_electric_001/v1"
os.makedirs(output_dir, exist_ok=True)


# ---------- SAVE FILES ----------
with open(f"{output_dir}/memo.json", "w") as f:
    json.dump(memo, f, indent=4)

with open(f"{output_dir}/agent_spec.json", "w") as f:
    json.dump(agent_spec, f, indent=4)

with open(f"{output_dir}/agent_prompt.txt", "w") as f:
    f.write(agent_prompt)


print("Files generated successfully.")