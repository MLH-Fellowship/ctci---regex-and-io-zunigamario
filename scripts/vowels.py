# Write the solution for "Filter Vowels".
import re
f = open("vowels.txt", "r").read()
letters = [l for l in f]
counter = 0
for i in letters:
    if re.match("[aeiouAEIOU]", i):
        # print("yoooo")
        counter += 1

w = open("vowels-" + str(counter) + ".txt", "w")
w.write(f)