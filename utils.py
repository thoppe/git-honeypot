import subprocess
from pathlib import Path
import time


class GitOperations:
    def __call__(self, cmd):
        r = subprocess.check_output(cmd, shell=True)
        return r.decode("utf-8").strip()

    def last_commit_hash(self) -> str:
        cmd = "git rev-parse HEAD"
        return self(cmd)

    def total_commits(self) -> int:
        cmd = "git rev-list HEAD --count"
        return int(self(cmd))

    def current_branch_name(self) -> str:
        cmd = "git symbolic-ref --short HEAD"
        return self(cmd)

    def garbage_collect(self) -> None:
        self("git gc")


class MeasuredOperation:
    def __init__(self, n_refactor=1_000):

        self.git = GitOperations()
        self.n_commits = self.git.total_commits()
        self.n_refactor = n_refactor

        self.t0 = time.monotonic()

        self.f_log = Path("status_log.csv")
        if not self.f_log.exists():
            with open(self.f_log, "w") as FOUT:
                FOUT.write(
                    "n_commits,directory_size,action_time,compress_time,interval_time\n"
                )

    def __len__(self) -> int:
        # Measures the total size of the local directory
        root_directory = Path(".")
        return sum(p.stat().st_size for p in Path(".").rglob("*"))

    def action(self):
        raise NotImplementedError

    def __call__(self):
        # Returns
        self.action()
        self.n_commits += 1

        if self.n_commits % self.n_refactor == 0:
            t0 = self.t0
            t1 = time.monotonic()

            self.git.garbage_collect()
            t2 = time.monotonic()

            directory_size = len(self)
            print("Filesize:", directory_size)

            line = f"{self.n_commits},{directory_size},{t1-t0},{t2-t1},{t2-t0}"
            with open(self.f_log, "a") as FOUT:
                FOUT.write(line + "\n")

            self.t0 = time.monotonic()
            print(line)
