import csv
import sys
import os


try:
    with open(sys.argv[1], 'r', encoding="utf8") as f:
        
        reader = csv.reader(f, doublequote=True)
        next(reader)
        title = next(reader)[0].title().replace(":", " ") # Replace : because windows doesn't support : in file names
        author = next(reader)[0][3:].title()
        print(title)
        print(author)

        try:

            with open(sys.argv[2] + os.sep + title + " - " + author + ".md", 'w', encoding="utf8") as md:
                md.write("# "+ title + " - " + author)
                md.write("\n\n")

                for i in range(5):
                    next(reader)
                for line in reader:
                    md.write("{} - {}".format(line[3], line[1]))
                    md.write("\n\n\n")

        except PermissionError:
            sys.exit("Do not have the rights to save file")

except FileNotFoundError:
    sys.exit("File not exists")