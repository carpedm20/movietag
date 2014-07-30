
push:
	git push -u origin master

count:
	ls data/ | wc -l

big:
	ls -alh data/ --sort=size | head -4000
