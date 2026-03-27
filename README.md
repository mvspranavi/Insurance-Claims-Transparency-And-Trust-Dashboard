# Insurance Claims Transparency & Trust Dashboard  

📊 This project demonstrates how data transparency builds trust in insurance claims.  
It combines **SQL queries, Python scripts, and Power BI dashboards** to analyze and visualize claims data.  

---

## 📂 Repository Structure
- **docs/** → Contains documentation  
  - BusinessRequirements.md  
  - DataDictionary.md  
  - UserStories.md  
  - ProcessFlow-instructions.md  
  - Queries.md  
- **src/** → Source code  
  - **data/** → Raw & cleaned claims data (`sample_claims.csv`, `claims_clean.csv`)  
  - **scripts/** → Python scripts (`generate_sample_claims.py`, `clean_data.py`)  
- **dashboards/** → Power BI dashboards (`InsuranceClaimsDashboard.pbix`)  

---

## ⚙️ Steps in Project
1. **Generated sample claims data** using Python (`generate_sample_claims.py`).  
2. **Cleaned data** and added SLA/Transparency metrics (`clean_data.py`).  
3. **Wrote SQL-style queries** with pandasql (`Queries.md`).  
4. **Built Power BI Dashboard** to visualize:  
   - Claims by Status (Approved, Denied, Pending)  
   - Denial Reasons  
   - SLA Breach %  
   - Transparency Score  
   - Total & Average Claim Amount  
