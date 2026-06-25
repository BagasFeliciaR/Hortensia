from sqlalchemy.orm import Session

from app.models.workflow import WorkflowStep


class WorkflowRepository:

    def create_steps(
        self,
        db: Session,
        job_id: int,
        steps: list[str],
    ):

        created = []

        for index, step in enumerate(steps):

            obj = WorkflowStep(
                job_id=job_id,
                step_order=index + 1,
                step_name=step,
            )

            db.add(obj)

            created.append(obj)

        db.commit()

        return created
