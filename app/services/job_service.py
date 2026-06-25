from app.database.database import SessionLocal
from app.repositories.job_repository import JobRepository
from app.services.workflow_service import WorkflowService


class JobService:

    def __init__(self):
        self.repo = JobRepository()
        self.workflow = WorkflowService()

    def create_job(
        self,
        job_type: str,
        payload: dict,
    ):

        db = SessionLocal()

        try:
            job = self.repo.create(
                db,
                job_type,
                payload,
            )

            print(f"[JOB] Created #{job.id}")

        finally:
            db.close()

        self.workflow.create_program_analysis(job.id)

        print(f"[WORKFLOW] Created for Job #{job.id}")

        return job
