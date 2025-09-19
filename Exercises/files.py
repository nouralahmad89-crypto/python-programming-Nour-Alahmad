# r: read
# a: append
# w: write
# x: create

# read: error if it doesn't excist
import re
import os

f= open("hello.txt", "r")
print(f.read())
