# Execution Engine

The execution engine is responsible for running external security tools.

Execution flow:

Execution Request

↓

Policy Validation

↓

Tool Registry

↓

Tool Adapter

↓

Process Runner

↓

Output Parser

↓

Audit Logger

↓

Workflow Update

Current implementation:

- httpx

Future adapters:

- subfinder
- katana
- gau
- waybackurls
- nuclei
- ffuf
