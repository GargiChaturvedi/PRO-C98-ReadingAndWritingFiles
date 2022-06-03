def swappingFileContent1(file1, file2):
    with open(file1, 'r') as a:
        data_a = a.read()
        a.close()
    with open(file2, 'r') as b:
        data_b = b.read()
        b.close()
    with open(file1, 'w') as a:
        a.write(data_b)
        a.close()
    with open(file2, 'w') as b:
        b.write(data_a)
        b.close()

    printA = open(file1, 'r')
    print("\nUpdated Contents for file 1:", printA.read())
    printB = open(file2, 'r')
    print("\nUpdated Contents for file 2:", printB.read())

file_1 = input("Enter file path for the first file: ")
file_2 = input("Enter file path for the second file: ")
swappingFileContent1(file_1, file_2)