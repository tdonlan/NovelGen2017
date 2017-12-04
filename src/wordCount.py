import sys

file1 = sys.argv[1]
print file1
file1text = open(file1,"r").read().split()

print len(file1text)