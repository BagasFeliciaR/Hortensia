from sqlalchemy.orm import Session

from app.models.job import Job


class JobRepository:

    def create(
        self,
        db: Session,
        job_type: str,
        payload: dict,
    ) -> Job:

        job = Job(
            type=job_type,
            payload=payload,
        )

        db.add(job)
        db.commit()
        db.refresh(job)

        return job
