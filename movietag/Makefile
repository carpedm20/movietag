
init:
	find ./ -name "migrations" -exec rm -rf {} \;
	./manage.py syncdb
	./manage.py schemamigration account --initial
	./manage.py schemamigration movie --initial
	./manage.py shell

migrate:
	./manage.py schemamigration movie --auto
	./manage.py schemamigration account --auto
	./manage.py migrate account
	./manage.py migrate movie

clean:
	rm db.sqlite3
	find ./ -name "migrations" -exec rm -rf {} \;
