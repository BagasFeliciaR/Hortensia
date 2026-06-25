from app.approval.service import ApprovalService

service = ApprovalService()

job = service.approve(1)

print(job.id)
print(job.status)
print(job.approved)
