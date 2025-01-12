def printFile(path, read_type='all'):
    try:
        with open(path, 'r') as file:
            if read_type == 'all':
                print(file.read())
            elif read_type == 'stroke':
                for line in file:
                    print(line, end='')
    except FileNotFoundError:
        print(f'Не удалось найти файл: {path}')


printFile('exampl.txt')
printFile('example.txt', 'stroke')
