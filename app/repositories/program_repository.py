from sqlalchemy.orm import Session

from app.models.program import Program


class ProgramRepository:

    def create(
        self,
        db: Session,
        name: str,
        platform: str,
        program_url: str,
        status: str,
    ) -> Program:

        program = Program(
            name=name,
            platform=platform,
            program_url=program_url,
            status=status,
        )

        db.add(program)
        db.commit()
        db.refresh(program)

        return program
