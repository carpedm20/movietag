#!/usr/bin/python
import json
import subprocess, shlex

PER_COUNT = 1000
cur_index = 0

f=open('movie_tag.json','r')
jj = json.loads(f.read())
f.close()

while True:
    tmp_list = jj[cur_index:cur_index + PER_COUNT]
    cur_index += PER_COUNT

    if tmp_list == []:
        break

    f_name = 'tmp.json'
    f = open(f_name,'w')
    json.dump(tmp_list, f)
    f.close()

    command_line = "mongoimport --db carpedm20 --collection movie --type json --jsonArray --file %s"

    print subprocess.check_output(shlex.split(command_line % f_name))
