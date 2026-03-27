# Data Dictionary – Insurance Claims Transparency & Trust Dashboard

This document defines all key fields used in the claims dataset for clarity and consistency.

---

## 📂 Claims Data Fields

- **ClaimID** → Unique identifier for each claim (string). Example: `C0001`  
- **CustomerID** → Unique identifier for each customer (string). Example: `U1234`  
- **Provider** → Name of the healthcare provider/clinic/hospital (string). Example: `CarePlus Hospital`  
- **State** → US state code where the claim originated (string). Example: `TX`  
- **SubmittedChannel** → How the claim was submitted (Portal, Email, Agent, Phone, EDI).  
- **ClaimDate** → Date claim was submitted (YYYY-MM-DD). Example: `2025-01-12`  
- **ClaimAmount** → Amount claimed in USD (decimal). Example: `2450.50`  
- **Status** → Current claim status (Approved, Denied, Pending).  
- **DenialReason** → Reason provided if the claim is denied (string). Example: `Missing Documentation`  
- **ProcessingTimeDays** → Total number of days to process claim (integer). Example: `12`  
- **SLA_Brea_**
