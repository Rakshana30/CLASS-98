def counting():
    fileName = input("Enter your file name")
    count = 0
    file = open(fileName,'r')
    for line in file:
        word = line.split()
        count = count+len(word)
    print("Number of word in the file")
    print(count)
counting()    