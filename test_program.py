from app.events.register import register_events
from app.services.program_service import ProgramService

register_events()

service = ProgramService()

program = service.create_program(
    name="DPG Media",
    platform="Intigriti",
    url="https://intigriti.com/programs/example",
)

print(program.id)
print(program.name)
