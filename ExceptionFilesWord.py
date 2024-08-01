def readFromFile(fileName: str):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        print(data)


print()


def wordCounter(fileName):
    nWords = 0
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        lines = data.split()
        for word in lines:
            if not word.isnumeric():
                nWords += 1
    return nWords


myFile = "./my_file.txt"

print("File content:")
readFromFile(myFile)

print(f"\nNumber of words: \t{wordCounter(myFile)}")
