import subprocess
import time

from app.tools.adapters.base import ExecutionResult


class ProcessRunner:

    def run(self, command, timeout=300):

        start = time.time()

        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
        )

        duration = round(time.time() - start, 3)

        return ExecutionResult(
            success=(process.returncode == 0),
            exit_code=process.returncode,
            stdout=process.stdout.strip(),
            stderr=process.stderr.strip(),
            command=command,
            duration=duration,
        )
