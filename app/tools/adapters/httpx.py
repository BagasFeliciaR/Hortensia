from app.execution.process.runner import ProcessRunner
from app.tools.adapters.base import ToolAdapter


class HttpxAdapter(ToolAdapter):

    name = "httpx"

    def __init__(self):
        self.runner = ProcessRunner()

    def run(self, request):

        command = [
            "httpx",
            *request.args,
        ]

        return self.runner.run(
            command,
            timeout=request.timeout,
        )
