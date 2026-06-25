from app.database.database import SessionLocal
from app.models.job import Job


class ApprovalService:

    def approve(self, job_id: int):

        db = SessionLocal()

        try:
            job = db.get(Job, job_id)

            if job is None:
                raise ValueError("Job not found")

            job.approved = True
            job.status = "APPROVED"

            db.commit()
            db.refresh(job)

            return job

        finally:
            db.close()

    def deny(self, job_id: int):

        db = SessionLocal()

        try:
            job = db.get(Job, job_id)

            if job is None:
                raise ValueError("Job not found")

            job.approved = False
            job.status = "DENIED"

            db.commit()
            db.refresh(job)

            return job

        finally:
            db.close()
