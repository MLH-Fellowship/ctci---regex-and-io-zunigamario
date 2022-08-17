# Write the solution for "Split the files".
import re

def splitter(file):
    f = re.split(" ", open(file, "r").read())

    counter = 1
    dot = file.index(".")
    print(dot)
    part1 = file[:dot] + "-"
    part2 = file[dot:]

    for i in f:
        curr = open(part1 + str(counter) + part2, "a")
        currtxt = open(part1 + str(counter) + part2, "r").read()
        if len(currtxt + i) < 500:
            curr.write(i + " ")
        else:
            counter += 1

splitter("github.txt")
splitter("meta.txt")





