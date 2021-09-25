def countWords():
    fileName = input("enter the file name ")

    f = open(fileName, "r")

    numberofwords = 0

    for line in f :
        words = line.split()
        numberofwords = numberofwords + len(words)

    print("Number of words: ")
    print(numberofwords)


countWords()