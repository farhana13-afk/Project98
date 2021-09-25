def countSentences():
    fileName = input("enter file name: ")

    f = open(fileName, "r")

    numberofsentences = 0

    for line in f : 
        sent = line.split(".")
        numberofsentences = numberofsentences + len(sent)
    
    print("Number of Sentences:")
    print(numberofsentences)

countSentences()
