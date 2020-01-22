#!/usr/bin/env python

import sys
import re

if len(sys.argv) != 3:
    print("Error: two arguments required.")
    print("")
    print("Usage: {} <arg1> <arg2>".format(sys.argv[0]))
    exit(0)

if not sys.argv[1].isnumeric():
    print("Error: the first argument must be a number")
    print("")
    print("Usage: {} <arg1> <arg2>".format(sys.argv[0]))
    exit(0)

if not sys.argv[2].isnumeric():
    print("Error: the second argument must be a number")
    print("")
    print("Usage: {} <arg1> <arg2>".format(sys.argv[0]))
    exit(0)

a = float(sys.argv[1])
b = float(sys.argv[2])

print (a + b)
