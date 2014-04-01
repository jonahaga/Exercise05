# open a file on command line
# count how many times each letter occurs in that file
# print the counts to the screen in alphabetical order
# use a dictionary

# Useful:
    # string.lower()
    # ord()

# argv allows you to open a file from the command line
from sys import argv

script, filename = argv

txt = open(filename)
filetext = txt.read()
txt.close()

d = {}

# Print one character at a time to the screen
for char in filetext:
    lowercase = char.lower()
    if ord(lowercase) >= ord('a') and ord(lowercase)<= ord('z'):
        if d.get(lowercase):
            d[lowercase] += 1
        else:
            d[lowercase] = 1

for key in sorted(d.keys()):
    print "%d" % (d[key])