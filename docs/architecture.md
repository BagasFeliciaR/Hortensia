# Architecture

## Overview

Hortensia is designed as an event-driven autonomous security platform.

Instead of directly executing tools, every action is represented as a workflow.

```
User

↓

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

Evidence

↓

Analysis

↓

Report
```

---

## Design Principles

### Modular

Every subsystem must be replaceable.

Example:

- AI Provider
- Tool Adapter
- Database Backend

must not require changes to unrelated modules.

---

### Event Driven

Subsystems communicate using events.

Examples:

```
program.created

↓

planner

↓

job.created

↓

worker

↓

execution.started
```

---

### Workflow First

Execution is never performed directly.

Everything must be represented as a workflow.

---

### Policy Aware

Every execution must respect program policy.

Examples:

- Scope
- Rate limit
- Allowed tools
- Manual approval

---

### Persistent

Every important action must be persisted.

Nothing important should only exist in memory.
