import pandas as pd
from pathlib import Path
import pylab as plt
import seaborn as sns

locations = {
    "branch_depth": "max_branch_depth",
    "branch_breadth": "max_branch_breadth",
    "commits": "max_commits",
    "empty_commits": "max_empty_commits",
}

aspect_ratio = 16 / 9

for key in ["compress_time", "interval_time", "action_time"]:
    plt.figure(figsize=(6 * aspect_ratio, 6))

    for k, v in locations.items():
        f_csv = Path(v) / "status_log.csv"
        df = pd.read_csv(f_csv)

        plt.plot(df['n_commits'], df[key], label=k, lw=4)

    plt.legend()
    sns.despine()
    plt.title(key)
    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(f"docs/{key}.png")

    print(df)


plt.show()
