# Process Flow – Insurance Claims Transparency & Trust Dashboard

This document explains the **end-to-end claims process** and how to draw it in a process flow diagram (using draw.io, Lucidchart, or similar tools).

---

## 📌 Steps in the Claims Process

**Swimlanes:** Customer → Intake → Claims Adjudication → QA/Review → Provider → Customer Support  

1. **Claim Submission**  
   - Customer submits claim via Portal, Email, Phone, Agent, or EDI.  

2. **Pre-Checks**  
   - System checks for completeness, eligibility, and duplicate claims.  

3. **Adjudication**  
   - Rules engine + manual review applied.  
   - Decision: Approve, Deny, or set as Pending (need more info).  

4. **Decision & Notification**  
   - If Approved → notify provider & customer, proceed to payment.  
   - If Denied → capture denial reason, notify provider & customer.  
   - If Pending → request missing documents.  

5. **SLA Monitoring**  
   - Check if processing time > 14 days → SLA breach flag.  

6. **Transparency Metrics Logged**  
   - SLA Breach %, Denial Reason, Transparency Score recorded for dashboards.  

---

## 📊 How to Draw the Diagram (instructions)

- Open **https://app.diagrams.net** (draw.io).  
- Add **swimlanes** for each role: Customer, Intake, Adjudication, QA, Provider, Support.  
- Add shapes for each step (submission, pre-check, adjudication, decision, SLA check).  
- Use **arrows** to connect the steps.  
- Highlight SLA (14 days) with a note.  
- Save the diagram as **ProcessFlow.png** and add it to `/docs`.  

---

## ✅ Output
- A clear **BPMN-style diagram** that explains the entire claims journey.  
- This diagram will make it easy for non-technical stakeholders to understand the workflow.
