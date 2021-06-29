import sys
from tqdm import tqdm
from utils import MeasuredOperation


class GitAdvanceCommit(MeasuredOperation):
    def action(self):

        n = self.n_commits
        cmd = f'git commit --allow-empty -m "{n}"'
        self.git(cmd)


model = GitAdvanceCommit()

# Take the next advancement from the command-line
n = int(sys.argv[1])

for _ in tqdm(range(n - model.n_commits)):
    model()
