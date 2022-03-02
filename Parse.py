import sys, os
import pysrt

def main(argv):
    path = argv[1]
    subs = pysrt.open(path)

    file = open("captions.txt", "w+")
    file.truncate(0)

    for sub in subs:
        file.write(sub.text)
        file.write("\n")

    file.close()
    print("Created captions.txt at: " + os.getcwd())

if __name__ == "__main__":
    main(sys.argv)
