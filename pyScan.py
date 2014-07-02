#! /bin/python

import sys
import pyclamd

cd = pyclamd.ClamdAgnostic()
result = cd.scan_file(sys.argv[1])
f = open('/home/dm/fiscanner/av.log', 'a')
f.write(sys.argv[1] + ": " + str(result) + "\n")
