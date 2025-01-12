def printFile(path, read_type='all'):
    with open(path, 'r') as file:
        if read_type == 'all':
            print(file.read())
        elif read_type == 'stroke':
            for line in file:
                print(line, end='')


printFile('example.txt')
printFile('example.txt', 'stroke')
