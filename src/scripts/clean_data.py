"""
clean_data.py
--------------------------------
This script cleans sample_claims.csv and adds new insights:
- SLA_Breached → Simulated randomly (since no ProcessingTimeDays column exists)
- IsApproved / IsDenied / IsPending → binary flags
- TransparencyScore → simple score (higher = better transparency)

Output: claims_clean.csv in /src/data/
"""

import pandas as pd
import random

# Load the raw claims data
df = pd.read_csv("../data/sample_claims.csv")

# Simulate SLA_Breached (random yes/no for now)
df["SLA_Breached"] = [random.choice([0, 1]) for _ in range(len(df))]

# Add binary flags
df["IsApproved"] = df["Status"].apply(lambda x: 1 if x == "Approved" else 0)
df["IsDenied"] = df["Status"].apply(lambda x: 1 if x == "Denied" else 0)
df["IsPending"] = df["Status"].apply(lambda x: 1 if x == "Pending" else 0)

# Transparency Score (100 - penalties)
df["TransparencyScore"] = 100 - (df["SLA_Breached"] * 20 + df["IsDenied"] * 10)

# Save cleaned data
df.to_csv("../data/claims_clean.csv", index=False)

print("✅ Cleaned data saved as claims_clean.csv in /src/data/")
