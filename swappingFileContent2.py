#Hello ma'am, finally both the pieces of code are functioning properly. Thanks for your guidance.
def swappingFileContent2(file1, file2):
    fileA = open(file1, 'r')
    fileB = open(file2, 'r')
    fileC = fileA.read()
    fileD = fileB.read()
    fileA.close()
    fileB.close()

    reopenA = open(file1, 'w')
    reopenB = open(file2, 'w')
    reopenA.write(fileD)
    reopenB.write(fileC)
    reopenA.close()
    reopenB.close()

    printA = open(file1, 'r')
    printB = open(file2, 'r')
    print("\nUpdated contents of first file: " + printA.read())
    print("Updated contents of second file: " + printB.read())

firstFile = input("Enter the path for the first file: ")
secondFile = input("Enter the path for the second file: ")
swappingFileContent2(firstFile, secondFile)