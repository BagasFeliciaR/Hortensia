from app.workflow.scheduler import WorkflowScheduler

scheduler = WorkflowScheduler()

step = scheduler.next_step()

print("=" * 40)

if step is None:
    print("No pending workflow.")
else:
    print("JOB ID    :", step.job_id)
    print("STEP      :", step.step_order)
    print("NAME      :", step.step_name)
    print("STATUS    :", step.status)

print("=" * 40)
