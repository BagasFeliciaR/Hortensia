from app.database.database import SessionLocal
from app.repositories.workflow_repository import WorkflowRepository


class WorkflowScheduler:
    def __init__(self):
        self.repo = WorkflowRepository()

    def next_step(self):
        db = SessionLocal()

        try:
            step = self.repo.get_next_pending_step(db)

            return step

        finally:
            db.close()
