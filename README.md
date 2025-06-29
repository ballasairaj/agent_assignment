# agent_assignment

🧠 Multi-Agent AI Document Router
📌 Objective
This project builds a multi-agent AI system that can:

Accept input in PDF, JSON, or Email (text) format.

Classify the format and intent (e.g., RFQ, Complaint, Invoice, etc.).

Route the input to the correct processing agent.

Maintain a shared context/memory for traceability and chaining.

🧭 System Overview
The system is composed of three agents and a shared memory module, orchestrated as follows:

1. 🤖 Classifier Agent
Input: Raw PDF / JSON / Email (text)

Responsibilities:

Detect the format: PDF / JSON / Email

Detect the intent: Invoice, RFQ, Complaint, Regulation, etc.

Log format + intent into memory

Route the input to the correct agent (EmailAgent or JSONAgent)

2. 🧾 JSON Agent
Input: Structured JSON payloads

Responsibilities:

Extract fields and transform into a standard schema

Flag anomalies or missing fields

Log extraction results into memory

3. 📧 Email Agent
Input: Plain text emails

Responsibilities:

Extract sender, intent, and urgency

Format the output for CRM-style usage

Log extracted information to memory

4. 🧠 Shared Memory Module
Stores and shares context between agents:

Source type and timestamp

Extracted values

Conversation/thread ID

Backed by: Redis, SQLite, or lightweight in-memory storage

