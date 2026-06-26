# Workflow Engine

Every operation inside Hortensia is represented as a workflow.

Example:

Program

↓

Policy Parser

↓

Scope Extractor

↓

Recon Planner

↓

Execution

↓

Evidence

↓

Analysis

↓

Report

Each step can be:

- Pending
- Running
- Success
- Failed
- Skipped

Future versions will support:

- Retry
- Resume
- Parallel execution
- Conditional branching
