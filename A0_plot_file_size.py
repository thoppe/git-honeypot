import pandas as pd
from pathlib import Path
import pylab as plt

locations = {
    "branch_depth": "max_branch_depth",
    "branch_breadth": "max_branch_breadth",
    "commits": "max_commits",
    "empty_commits": "max_empty_commits",
}

for k, v in locations.items():
    f_csv = Path(v) / "status_log.csv"
    df = pd.read_csv(f_csv)

    # plt.plot(df.compress_time, label=k)
    # plt.plot(df.interval_time, label=k)
    plt.plot(df.action_time, label=k)

    print(df)

plt.legend()
plt.show()
