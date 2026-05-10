# Telecom Support Bot — Dialogflow CX + Flask + MySQL

## Project Overview

This project is an enterprise-style telecom customer support chatbot built using Dialogflow CX, Flask webhook services, and MySQL database integration.

The bot supports:

* Customer authentication using OTP flow
* Complaint registration
* Balance inquiry
* Fallback handling
* Escalation handling
* Webhook-based backend integration
* MySQL complaint storage
* CI/CD testing preparation

---

# Architecture

```text
User
 ↓
Dialogflow CX
 ↓
Flask Webhook API
 ↓
MySQL Database
```

---

# Technologies Used

| Technology                   | Purpose                      |
| ---------------------------- | ---------------------------- |
| Dialogflow CX                | Conversational AI platform   |
| Python Flask                 | Webhook backend              |
| MySQL                        | Persistent complaint storage |
| GitHub                       | Source control               |
| GitHub Actions               | CI/CD pipeline               |
| Ngrok / Deployment Platforms | Public webhook exposure      |

---

# Features Implemented

## 1. Authentication Flow

Implemented OTP-based authentication flow using Dialogflow CX pages and Flask webhook validation.

### Flow

```text
Login
 ↓
Collect Mobile Number
 ↓
Send OTP
 ↓
Verify OTP
 ↓
Authentication Success / Failure
```

### Concepts Learned

* Session parameters
* Conditional routing
* Webhook validation
* Authentication gating
* Multi-page conversational flows

---

## 2. Complaint Registration Flow

Users can raise complaints after authentication.

### Workflow

```text
Raise Complaint
 ↓
Webhook Trigger
 ↓
Generate Ticket ID
 ↓
Store Complaint in MySQL
 ↓
Return Success Response
```

### Sample Ticket

```text
TKT1099
```

---

## 3. Balance Inquiry Flow

Implemented dynamic balance checking using webhook logic.

### Logic

* Mobile number validated
* Dynamic balance returned from backend logic

---

## 4. Webhook Integration

Created Flask webhook service to process:

* Complaint creation
* OTP validation
* Balance inquiry
* Dynamic responses

### Key Concept

Dialogflow CX handles NLP and conversation management,
while Flask handles business logic.

---

## 5. MySQL Database Integration

Complaint data is stored in MySQL.

### Complaint Table Structure

| Column     | Purpose                |
| ---------- | ---------------------- |
| ticket_id  | Unique complaint ID    |
| mobile     | Customer mobile number |
| issue      | Complaint description  |
| status     | Complaint status       |
| created_at | Timestamp              |

---

## 6. Fallback Handling

Implemented enterprise fallback handling using:

### Events

* no-match-default
* no-input-default

### Responses

```text
Sorry, I didn’t understand that. Can you rephrase?
```

### Escalation

Repeated failures transition to:

```text
Agent Escalation Page
```

---

# Dialogflow CX Concepts Implemented

| Concept           | Usage                    |
| ----------------- | ------------------------ |
| Intents           | User intention detection |
| Entities          | Extracting values        |
| Parameters        | Session data storage     |
| Pages             | Conversation steps       |
| Flows             | Business workflows       |
| Transition Routes | Navigation logic         |
| Event Handlers    | Error recovery           |
| Webhooks          | Backend integration      |

---

# Flask Webhook Features

Implemented:

* Dynamic ticket generation
* OTP validation
* API response handling
* JSON request/response processing
* MySQL insertion logic

---

# CI/CD Preparation

Prepared:

* requirements.txt
* GitHub repository structure
* GitHub Actions workflow
* Unit test preparation

### Sample CI Validation

* Flask syntax validation
* Dependency installation
* Webhook API testing
* Database integration testing

---

# Cloud & Enterprise Concepts Learned

## Cloud Deployment

Learned how Flask webhook services can be deployed using:

* Render
* Cloud Run
* Railway

using HTTPS webhook endpoints.

---

## Logging & Monitoring

Explored:

* Cloud Logging
* Logs Explorer
* BigQuery analytics

for enterprise chatbot observability.

---

# Sample Interview Explanation

```text
I developed a telecom support chatbot using Dialogflow CX.
The bot supports authentication, complaint registration,
balance inquiry, fallback handling, and escalation workflows.

I integrated Dialogflow CX with a Flask webhook backend
for dynamic business logic and MySQL database operations.

The webhook handles ticket generation, OTP validation,
and complaint storage.

I also implemented fallback recovery,
session handling,
and enterprise conversational architecture concepts.
```

---

# Folder Structure

```text
telecom-bot-project/
│
├── dialogflow-agent/
│     └── exported-agent.json
│
├── webhook/
│     ├── app.py
│     ├── requirements.txt
│     ├── test_app.py
│     └── python-app.yml
│
├── database/
│     └── schema.sql
│
└── README.md
```

---

# Future Enhancements

Planned enterprise improvements:

* Redis session management
* JWT authentication
* Cloud Run deployment
* Docker containerization
* BigQuery analytics
* Monitoring dashboards
* Live agent integration
* Rate limiting
* Kubernetes deployment

---

# Key Learning Outcomes

This project provided hands-on exposure to:

* Enterprise chatbot architecture
* Backend API integration
* Session management
* Authentication workflows
* Database persistence
* Error handling and escalation
* CI/CD concepts
* Cloud deployment understanding

---

# Author

Telecom Support Bot Project
Built using Dialogflow CX + Flask + M
