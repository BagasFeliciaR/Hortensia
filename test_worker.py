import threading

from app.events.register import register_events

from app.services.program_service import ProgramService

from app.workers.planner_worker import start


threading.Thread(
    target=start,
    daemon=True,
).start()

register_events()

service = ProgramService()

service.create_program(
    name="DPG Media",
    platform="Intigriti",
    url="https://intigriti.com",
)

input()
