# 📊 RBQL Queries for Sample Claims Data

```sql
SELECT * LIMIT 10

SELECT a.ClaimID, a.Provider, a.DenialReason 
WHERE a.Status == "Denied"

SELECT a.Provider, COUNT(*) 
GROUP BY a.Provider

SELECT a.Status, AVG(a.Amount)
GROUP BY a.Status

SELECT a.ClaimID, a.Provider, a.Amount 
ORDER BY a.Amount DESC 
LIMIT 5

### Below query shows Average transperancy score per provider.

SELECT a.Provider, AVG(float(a.TransparencyScore)) GROUP BY a.Provider
