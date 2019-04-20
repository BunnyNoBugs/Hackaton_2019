import re

def strip_saying(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.readlines()
    for i, line in enumerate(text):
        text[i] = line.split('\t')
        for j, half in enumerate(text[i]):
            text[i][j] = text[i][j].rstrip('\n ')
    print(text)
    with open('sayings.tsv', 'w') as f:
        for line in text:
            f.write('\t'.join(line) + '\n')





def main():
    strip_saying('поговорки - все вместе.tsv')


if __name__ == '__main__':
    main()