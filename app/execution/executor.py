from dataclasses import dataclass

from app.audit.logger import AuditLogger
from app.tools.registry.tool_registry import ToolRegistry


@dataclass
class ExecutionRequest:
    tool: str
    args: list[str]
    require_approval: bool = False
    timeout: int = 300


class ExecutionEngine:

    def __init__(self):
        self.registry = ToolRegistry()
        self.audit = AuditLogger()

    def execute(self, request):
        adapter = self.registry.get(request.tool)

        if adapter is None:
            raise ValueError(
                f"Tool '{request.tool}' is not registered."
            )

        result = adapter.run(request)

        self.audit.log(result)

        return result
