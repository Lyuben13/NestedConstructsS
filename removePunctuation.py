punctuationSymbols = r"!()-;?@#$%:'\"\./*_"


def removePunctuation(myStr, marks) -> str:
    resultStr = ""
    for symbol in myStr:
        if symbol not in marks:
            resultStr += symbol
    return resultStr


def reverseFileWords(fileName: str):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        data = removePunctuation(data, punctuationSymbols)
        words = data.split()
        reverseWords = reversed(words)

        for word in reverseWords:
            print(word)


myFile = "./my_file.txt"

reverseFileWords(myFile)
