# Database

Hortensia uses PostgreSQL as its primary database.

## programs

Stores bug bounty program metadata.

Columns:

- id
- name
- platform
- url
- status

---

## jobs

Represents every workflow execution.

Columns:

- id
- type
- status
- approval_required
- approved

---

## workflow_steps

Stores workflow execution state.

---

## discoveries

Stores normalized outputs from every tool.

---

## evidence

Stores evidence collected during execution.

---

## findings

Stores validated security findings.

---

## reports

Stores generated reports.

---

## audit_logs

Stores audit trail.
