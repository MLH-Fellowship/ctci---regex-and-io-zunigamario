# Write the solution for "Longest Word".
import re
f = re.split(" ", open("longest.txt", "r").read())
long = 0
for i in f:
    z = re.match("\b\w{40}\b", i)
    if z:
        print(z)
    if len(i) > long:
        long = len(i)

print("longest: " + str(long))

w = open("longest.txt", "w")
for i in f:
    if len(i) == long:
        i = re.sub(i, "**" + i + "**", i)
    w.write(i + " ")






