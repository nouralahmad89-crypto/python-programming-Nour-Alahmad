# r: read
# a: append
# w: write
# x: create

# read: error if it doesn't excist
import re
import os

f= open("c:\My Repo\python-programming-Nour-Alahmad\Exercises\hello.txt", "r")
#print(f.read())
#print(f.read(4))
#print(f.readline())
#print(f.readline())
for line in f:
    print(line)
f.close()

try: 
   f = open("c:\My Repo\python-programming-Nour-Alahmad\Exercises\hello1.txt", "r")
   print(f.read())
except:
    print("file not found")
finally:
    f.close()
#append to file, create the file if it dosen't exsist
f= open("c:\My Repo\python-programming-Nour-Alahmad\Exercises\hello.txt", "a")
f.write("\nNeil")
f.close()
f= open("c:\My Repo\python-programming-Nour-Alahmad\Exercises\hello.txt", "r")
print(f.read())
f.close()
file_path = r"C:\My Repo\python-programming-Nour-Alahmad\Exercises\hello.txt"

with open(file_path, "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    line = line.strip()  # remove \n
    if line == "JinneyNeil":  # line with the stuck name
        new_lines.append("Jinney")  # keep Jinney
        # Do NOT append Neil here, because you want to keep only the last Neil
    else:
        new_lines.append(line)
