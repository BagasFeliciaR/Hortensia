from pathlib import Path
from datetime import datetime


class AuditLogger:

    def __init__(self):
        self.log_dir = Path("logs")
        self.log_dir.mkdir(exist_ok=True)

    def log(self, result):

        logfile = self.log_dir / "execution.log"

        with open(logfile, "a") as f:

            f.write("=" * 70 + "\n")
            f.write(f"TIME      : {datetime.now()}\n")
            f.write(f"COMMAND   : {' '.join(result.command)}\n")
            f.write(f"SUCCESS   : {result.success}\n")
            f.write(f"EXIT CODE : {result.exit_code}\n")
            f.write(f"DURATION  : {result.duration} sec\n\n")

            f.write("STDOUT\n")
            f.write(result.stdout)
            f.write("\n\n")

            f.write("STDERR\n")
            f.write(result.stderr)
            f.write("\n\n")
