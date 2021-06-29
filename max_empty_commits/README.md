# Git Honeypot: Max empty commits

A git repo designed to test the maximum number of empty commits a repo can have.
Each commit updates with `--allow-empty`

Why? Designed to examine problems with automated scanners and git interfaces like github.

### [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law)
_When a measure becomes a target, it ceases to be a good measure._

+ [Linux repo](https://github.com/torvalds/linux) 1,014,975 commits
+ [Commited](https://github.com/virejdasani/Commited) 3 million empty commits

### Size ratio:

Number of commits | Repo size (in K) running 'git gc' after every 1000
------------------------------
1      | 172
10     | 172
100    | 200
1000   | 552
10000  | 4000 (time 0:30)
100000 | 38000 (time 5:53)
