def removeLine(fileIn, fileOut, lineNumber):
    with open(fileIn) as fr:
        lines = fr.readline()

        counter = 1

        with open(fileOut, 'w') as fw:
            for line in lines:
                if counter != lineNumber:
                    fw.write(line)
                counter += 1


myFile = "./my_file.txt"
resultFile = "./resultFile.txt"

removeLine(myFile, resultFile, 0)
