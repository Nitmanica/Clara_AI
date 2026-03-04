Clara Answers – AI Agent Automation Pipeline
Overview
This project implements an automated pipeline that converts demo call transcripts into deployable AI voice agent configurations for service businesses such as electrical, fire protection, HVAC, and maintenance companies.

The system extracts operational information from demo calls and generates structured configurations that can be used to deploy a Retell AI voice agent.

The workflow supports versioned agent updates when onboarding information becomes available.

System Architecture
Demo Call Transcript
        ↓
Extraction Pipeline
        ↓
Account Memo (JSON)
        ↓
Agent Prompt Generator
        ↓
Retell Agent Specification
        ↓
Voice Agent Deployment
Project Structure
Clara_agent
│
├── data
│   └── demo_calls
│       └── ben_electric_demo.txt
│
├── scripts
│   ├── extract_demo_data.py
│   ├── generate_agent_prompt.py
│   └── update_agent_version.py
│
├── outputs
│   └── accounts
│       └── ben_electric_001
│           ├── v1
│           │   ├── memo.json
│           │   ├── agent_spec.json
│           │   └── agent_prompt.txt
│           │
│           └── v2
│               ├── memo.json
│               └── changes.json
│
├── workflows
│   └── workflow.json
│
└── README.md
Pipeline Components
1. Transcript Extraction

Script:

extract_demo_data.py

This script processes demo call transcripts and extracts structured information including:

company name

services offered

routing logic

business hours

emergency conditions

Output:

memo.json
2. Agent Prompt Generation

Script:

generate_agent_prompt.py

This script converts the structured memo into an AI agent prompt.

Output:

agent_prompt.txt

The prompt defines how the AI receptionist handles customer calls.

3. Retell Agent Specification

The system generates a Retell-compatible agent configuration.

Output:

agent_spec.json

This configuration includes:

agent name

voice style

business rules

system prompt

In production this configuration would be sent to the Retell API to deploy a voice agent.

4. Agent Versioning

Script:

update_agent_version.py

This script creates versioned updates of the agent configuration.

Example:

v1 → initial demo configuration
v2 → onboarding updates

Change history is stored in:

changes.json
Automation Workflow (n8n)

The pipeline can be orchestrated using n8n automation.

Workflow steps:

Manual Trigger
      ↓
Extract Demo Data
      ↓
Generate Agent Prompt
      ↓
Update Agent Version

Workflow definition is stored in:

workflows/workflow.json
Retell Integration

The generated agent_prompt.txt is used as the system prompt for a Retell Voice Agent.

In production deployment:

agent_spec.json → Retell API → Voice Agent

Due to the zero-cost constraint of this assignment, the deployment step is demonstrated through manual prompt insertion into Retell.

Running the Pipeline

From the project root:

python scripts/extract_demo_data.py
python scripts/generate_agent_prompt.py
python scripts/update_agent_version.py

Outputs will be stored in:

outputs/accounts/
Key Design Principles

The system follows several important design principles:

No hallucinated data

Explicit handling of missing information

Versioned agent configurations

Reproducible automation pipeline

Structured operational schema

Future Improvements

Potential improvements include:

automatic transcription of audio calls

automated Retell API deployment

database storage (Supabase)

dashboard for agent configuration

batch processing of multiple accounts

Conclusion

This project demonstrates how conversational data from sales and onboarding calls can be transformed into structured operational rules and deployed as AI voice agents for service businesses.

The pipeline enables scalable automation for configuring AI receptionists across multiple clients.
