#! /bin/python

import sys
import pyclamd

cd = pyclamd.ClamdAgnostic()
result = cd.scan_file(sys.argv[1])

if result != "None":
	print(result)
