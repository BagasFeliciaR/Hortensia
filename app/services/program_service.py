from app.database.database import SessionLocal
from app.events.bus import event_bus
from app.repositories.program_repository import ProgramRepository


class ProgramService:

    def __init__(self):
        self.repo = ProgramRepository()

    def create_program(
        self,
        name: str,
        platform: str,
        program_url: str,
        status: str,
    ):

        db = SessionLocal()

        try:

            program = self.repo.create(
                db=db,
                name=name,
                platform=platform,
                program_url=program_url,
                status=status,
            )

            event_bus.publish(
                "program.created",
                {
                    "id": program.id,
                    "name": program.name,
                    "platform": program.platform,
                },
            )

            return program

        finally:
            db.close()
