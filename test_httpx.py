from app.execution.executor import (
    ExecutionEngine,
    ExecutionRequest,
)

engine = ExecutionEngine()

result = engine.execute(
    ExecutionRequest(
        tool="httpx",
        args=[
            "-u",
            "https://example.com",
            "-silent",
        ],
    )
)

print("=" * 40)
print("SUCCESS :", result.success)
print("EXIT    :", result.exit_code)
print("COMMAND :", " ".join(result.command))
print("DURATION:", result.duration, "seconds")
print()
print("STDOUT")
print(result.stdout)
print()
print("STDERR")
print(result.stderr)
print("=" * 40)
