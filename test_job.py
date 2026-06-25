from app.services.job_service import JobService

service = JobService()

job = service.create_job(
    job_type="PROGRAM_ANALYSIS",
    payload={
        "program_id": 1
    }
)

print(job.id)
