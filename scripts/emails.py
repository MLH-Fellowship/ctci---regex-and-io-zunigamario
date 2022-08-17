# Write the solution for "New Emails".
import re
newf = open("replacement.csv", "x")
with open("emails.csv", "r") as f:
    for line in f:
        print("before:" + line)
        line = re.sub("gmail.com", "mlh.io", line)
        print("after:" + line)
        newf.write(line)


