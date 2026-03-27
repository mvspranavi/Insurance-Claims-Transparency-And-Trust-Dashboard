import pandas as pd
import random
import os

# This function will create fake claims
def generate_claims(num_records=20):
    providers = ["Provider A", "Provider B", "Provider C"]
    statuses = ["Approved", "Denied", "Pending"]
    denial_reasons = ["Incomplete Docs", "Policy Expired", "Not Covered"]

    data = []
    for i in range(1, num_records + 1):
        status = random.choice(statuses)
        denial_reason = random.choice(denial_reasons) if status == "Denied" else None
        data.append({
            "ClaimID": f"C{i:03d}",
            "Provider": random.choice(providers),
            "Amount": round(random.uniform(100, 5000), 2),
            "Status": status,
            "DenialReason": denial_reason
        })

    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_claims(30)
    # Ensure the data directory exists before saving
    os.makedirs("../data", exist_ok=True)
    df.to_csv("../data/sample_claims.csv", index=False)
    print("✅ Sample claims data generated and saved to data/sample_claims.csv")