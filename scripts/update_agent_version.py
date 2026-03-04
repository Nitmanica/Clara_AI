import json
import os

account_id = "ben_electric_001"

v1_path = f"outputs/accounts/{account_id}/v1/memo.json"

with open(v1_path, "r") as f:
    memo_v1 = json.load(f)

# copy previous memo
memo_v2 = memo_v1.copy()

# example onboarding update
memo_v2["business_hours"] = {
    "days": ["Mon","Tue","Wed","Thu","Fri"],
    "start": "08:00",
    "end": "17:00",
    "timezone": "America/Calgary"
}

# create v2 folder
v2_dir = f"outputs/accounts/{account_id}/v2"
os.makedirs(v2_dir, exist_ok=True)

# save new memo
with open(f"{v2_dir}/memo.json", "w") as f:
    json.dump(memo_v2, f, indent=4)

# create changelog
changes = {
    "changes": [
        {
            "field": "business_hours",
            "old": memo_v1.get("business_hours"),
            "new": memo_v2["business_hours"],
            "reason": "Updated during onboarding"
        }
    ]
}

with open(f"outputs/accounts/{account_id}/changes.json", "w") as f:
    json.dump(changes, f, indent=4)

print("v2 memo and changelog created.")