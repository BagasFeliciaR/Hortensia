from app.database.database import SessionLocal
from app.repositories.workflow_repository import WorkflowRepository


class WorkflowService:

    def __init__(self):
        self.repo = WorkflowRepository()

    def create_program_analysis(self, job_id: int):

        db = SessionLocal()

        try:

            self.repo.create_steps(
                db,
                job_id,
                [
                    "Policy Parser",
                    "Scope Extractor",
                    "Recon Planner",
                    "Approval",
                    "Tool Execution",
                    "Evidence Collection",
                    "AI Analysis",
                    "Report Builder",
                ],
            )

        finally:
            db.close()
