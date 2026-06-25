from app.services.program_service import ProgramService

service = ProgramService()

program = service.create_program(
    name="Test Program",
    platform="HackerOne",
    program_url="https://example.com",
    status="ACTIVE",
)

print("=" * 40)
print("ID       :", program.id)
print("NAME     :", program.name)
print("PLATFORM :", program.platform)
print("URL      :", program.program_url)
print("STATUS   :", program.status)
print("=" * 40)
