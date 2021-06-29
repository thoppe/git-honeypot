import sys
from tqdm import tqdm
from utils import MeasuredOperation


class GitAdvanceCommit(MeasuredOperation):
    def action(self):

        hx = self.git.last_commit_hash()
        n = self.n_commits
        branch_name = "master"

        cmd = f"git checkout -b {hx}_{n} {branch_name} --quiet"
        self.git(cmd)

        with open("HASH_CHANGE.txt", "w") as FOUT:
            FOUT.write(hx)

        cmd = f'git commit -a -m "{n}"'
        self.git(cmd)


model = GitAdvanceCommit()

# Take the next advancement from the command-line
n = int(sys.argv[1])

for _ in tqdm(range(n - model.n_commits)):
    model()
