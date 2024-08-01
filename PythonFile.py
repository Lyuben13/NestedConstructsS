def replaceTextInFile(fileName: str, orginText: str, newText: str):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        data = data.replace(orginText, newText)

    with open(fileName, 'w') as fileHandler:
        fileHandler.write(data)


def readFromFile(fileName):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        print(data)


myFile = './my_file.txt'

print("Original file content:")
readFromFile(myFile)

replaceTextInFile(myFile, 'Python', 'JavaScript')

print("\nNew file content:")
readFromFile(myFile)
