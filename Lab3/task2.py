from sys import stdin


def writeFile(text, clear=False):
    with open('user_input.txt', 'w' if clear else 'a') as file:
        for line in text:
            file.write(line)


lines = []
for line in stdin:
    lines.append(line)
writeFile(lines, True)
