#!/usr/bin/python
import sys
import getpass
from time import gmtime, strftime
from ndrive import Ndrive

if len(sys.argv) != 2:
    print "[!] Error: need file name"
    sys.exit(1)

f_name = sys.argv[1]
day = strftime("%Y-%m-%d", gmtime())

print "[*] Uploading %s" % f_name

nd = Ndrive()

#n_id = raw_input("Id : ")
n_id = "carpedm30"
n_pass = getpass.getpass()

nd.login(n_id, n_pass)
nd.uploadFile(f_name, "/%s-%s" % (day, f_name))

print "[*] Complete!"
