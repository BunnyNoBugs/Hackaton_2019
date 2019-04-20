import re
import random


def strip_saying(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    text = text.split('\n')
    first_halves = []
    second_halves = []
    for line in text:
        temp = line.split('\t')
        first_halves.append(temp[0])
        second_halves.append(temp[1])
    with open('first_halves.txt', 'w') as f:
        for half in first_halves:
            f.write(re.sub('\|.+?}', '}', half) + '\n')
    with open('second_halves.txt', 'w') as f:
        for half in second_halves:
            f.write(re.sub('\|.+?}', '}', half) + '\n')


def main():
    strip_saying('pogovorka.csv')


if __name__ == '__main__':
    main()