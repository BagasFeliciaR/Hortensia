# Hortensia

Hortensia is an autonomous AI security platform designed for bug bounty and authorized penetration testing.

Instead of acting as a launcher for security tools, Hortensia manages the entire assessment lifecycle: understanding program rules, planning workflows, executing tools, collecting evidence, analyzing results, and generating new hypotheses for further investigation.

The long-term goal is to provide a platform capable of running continuous, policy-aware security assessments while remaining compliant with the target program's rules.

> **Status**
>
> This project is currently under active development and is not ready for production use.

---

# Why Hortensia?

Most automation frameworks execute a predefined sequence of tools.

For example:

```
subfinder
    ↓
httpx
    ↓
katana
    ↓
nuclei
```

This approach works well for simple automation but has several limitations:

- no understanding of bug bounty policy
- no workflow orchestration
- no long-term memory
- no evidence management
- no adaptive planning

Hortensia is designed differently.

The execution pipeline is driven by workflows instead of static scripts.

```
Program
    ↓
Policy
    ↓
Planning
    ↓
Workflow
    ↓
Execution
    ↓
Analysis
    ↓
Evidence
    ↓
Report
```

---

# Current Features

## Program Management

- Store bug bounty programs
- Manage program metadata
- Store platform information
- Store program URLs

---

## Job System

Every operation inside Hortensia is represented as a Job.

Current workflow:

```
Program
    ↓
Create Job
    ↓
Generate Workflow
    ↓
Execute Steps
```

Job status currently supports:

- PENDING
- WAITING_APPROVAL
- APPROVED
- RUNNING
- SUCCESS
- FAILED
- DENIED

---

## Workflow Engine

Each job is divided into workflow steps.

Example:

```
Policy Parser

↓

Scope Extractor

↓

Recon Planner

↓

Approval

↓

Tool Execution

↓

Evidence Collection

↓

AI Analysis

↓

Report Builder
```

Workflow execution is designed to become resumable and fault tolerant.

---

## State Machine

Job state transitions are controlled by a dedicated state machine.

Invalid transitions are rejected.

Example:

```
PENDING

↓

WAITING_APPROVAL

↓

APPROVED

↓

RUNNING

↓

SUCCESS
```

---

## Execution Engine

Hortensia executes tools through adapters.

Instead of calling subprocesses directly throughout the project, every supported tool is wrapped by an adapter.

Current implementation:

- httpx

Future adapters:

- subfinder
- katana
- dnsx
- naabu
- gau
- waybackurls
- nuclei
- ffuf
- subjs
- uncover

---

## Tool Registry

Every tool is registered through a central registry.

```
Execution Engine

↓

Tool Registry

↓

Tool Adapter

↓

Process Runner
```

This allows tools to be added without changing the execution engine.

---

## Process Runner

Responsible for:

- subprocess execution
- timeout handling
- stdout capture
- stderr capture
- execution timing
- exit codes

---

## Approval System

Certain workflow steps can require manual approval before execution.

The approval system is intended to support bug bounty programs that restrict automated testing.

---

## Audit Logging

Every tool execution is recorded.

Current audit information includes:

- execution time
- executed command
- exit code
- duration
- stdout
- stderr

---

## Discord Interface

Current interface:

- Program submission modal
- Program creation
- Database integration

Additional interfaces planned:

- REST API
- CLI
- Web Dashboard

---

# Project Structure

```
app/

approval/
audit/
config/
database/
discord/
events/
execution/
models/
queue/
repositories/
services/
tools/
workers/

tests/
migrations/
```

---

# Technology Stack

Backend

- Python 3.12
- SQLAlchemy
- Alembic
- PostgreSQL

Interface

- Discord.py

Database

- PostgreSQL

---

# Roadmap

## Phase 1 — Foundation

- [x] Database
- [x] Repository Layer
- [x] Service Layer
- [x] Job System
- [x] Workflow Steps
- [x] State Machine
- [x] Tool Registry
- [x] Execution Engine
- [x] Process Runner
- [x] Discord Integration

---

## Phase 2 — Orchestration

- [ ] Workflow Scheduler
- [ ] Queue Persistence
- [ ] Retry Strategy
- [ ] Resume Support
- [ ] Dependency Graph

---

## Phase 3 — Policy Engine

- [ ] Policy Parser
- [ ] Scope Parser
- [ ] Global Rate Limiter
- [ ] Tool Restrictions
- [ ] Automation Constraints

---

## Phase 4 — Tool Ecosystem

- [ ] ProjectDiscovery integration
- [ ] ffuf
- [ ] nuclei
- [ ] JavaScript analysis
- [ ] API discovery

---

## Phase 5 — Intelligence

- [ ] Knowledge Engine
- [ ] Skill Engine
- [ ] Asset Graph
- [ ] Technology Fingerprinting
- [ ] Hypothesis Generation

---

## Phase 6 — Autonomous Operation

- [ ] Continuous assessment
- [ ] Evidence correlation
- [ ] AI-assisted planning
- [ ] Automatic reporting
- [ ] Memory Engine

---

# Current Development Status

This repository currently focuses on building the core architecture required for long-running autonomous security workflows.

The current implementation should be considered an engineering foundation rather than a complete security tool.

---

# Contributing

The project is under active development.

Issues, discussions, architecture suggestions, and pull requests are welcome.

---

# License

Apache License 2.0
