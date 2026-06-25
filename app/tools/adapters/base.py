from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ExecutionResult:

    success: bool
    exit_code: int
    stdout: str
    stderr: str
    command: list[str]
    duration: float


class ToolAdapter(ABC):

    name = ""

    @abstractmethod
    def run(self, request):
        pass
