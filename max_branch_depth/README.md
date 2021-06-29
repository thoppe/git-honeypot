# Git Honeypot: Max non-empty commits

A git repo designed to test the maximum number of non-empty commits a repo can have.
Each commit updates the file `HASH_CHANGE.txt` with the hash of the previous commit.

Why? Designed to examine problems with automated scanners and git interfaces like github.

### [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law)
_When a measure becomes a target, it ceases to be a good measure._

Not that total commits is rarely a good measure. Is this repo this


### Size ratio:

Number of commits | Repo size (in K) running 'git gc' after every 100
------------------------------
1      | 168
10     | 176
100    | 236
1000   | 860
10000  | 7000 (time 4:37)
100000 | 


Number of commits | Repo size (in K) without running 'git gc'
------------------------------
1     | 172
10    | 416
100   | 2100
1000  | 14000
10000 | 32000

After 1500+ commits, git auto runs `git gc` and gives "Auto packing the repository in background for optimum performance".


### Useful commands:

List total number of commit:

    git rev-list HEAD --count