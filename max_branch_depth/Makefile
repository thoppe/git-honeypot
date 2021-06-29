total_actions = 1000000

restart:
	rm -f HASH_CHANGE.txt status_log.csv
	touch HASH_CHANGE.txt
	rm -rvf .git/
	git init
	git add README.md advance.py utils.py HASH_CHANGE.txt
	git commit -m "1"
	git gc
	du -h

start:
	python advance.py $(total_actions)
