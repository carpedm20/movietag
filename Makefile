
push:
	git push -u origin master

count:
	ls data/ | wc -l

big:
	ls -alh data/ --sort=size | head -4000

mongoexport:
	mongoexport -d carpedm20 -c movie -o domain-bk.json

mongoimport:
	mongoimport -d carpedm20 -c movie --file domain-bk.json
