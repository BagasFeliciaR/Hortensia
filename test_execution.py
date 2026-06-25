from app.execution.executor import (
    ExecutionEngine,
    ExecutionRequest,
)

engine = ExecutionEngine()

engine.execute(
    ExecutionRequest(
        tool="httpx",
        args=[
            "-u",
            "https://example.com",
        ],
    )
)
