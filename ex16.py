from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you don't want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating that shit, son! Byeeee!")
target.truncate()

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print("And finally, we close that shit.")
target.close()