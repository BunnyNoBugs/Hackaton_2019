import re
import random


with open('sayings.tsv', encoding='utf-8') as f:
    originals = f.read()


codes = ('пов,2-л',
         'нп=непрош,ед,изъяв,3-л',
         'мн,изъяв,1-л',
         'ед,кр,муж',
         'нп=непрош,ед,изъяв,3-л,сов',
         'нп=непрош,ед,изъяв,3-л,несов',
         'прош,мн,изъяв,сов,пе',
         'прош,мн,изъяв,сов,пе',
         'нп=прош,ед,изъяв,сред,сов',
         '=V,пе=инф,несов')


def generator(first_halves, second_halves):
    possible_first = []
    possible_second = []
    code = random.choice(codes)
    if code != '—':
        for i, half in enumerate(second_halves):
            if code in half:
                possible_second.append(half)
                first_halves[i] = first_halves[i] + '{' + code + '}'
                possible_first.append(first_halves[i])
        for half in first_halves:
            if code in half:
                possible_first.append(half)
    else:
        for i, half in enumerate(first_halves):
            if code in half:
                possible_first.append(half)
                second_halves[i] = second_halves[i] + '{' + code + '}'
                possible_second.append(second_halves[i])
    saying = random.choice(possible_first) + ' ' + random.choice(possible_second)
    return saying


def clean_output(saying):
    saying = re.sub('{.+?}', '', saying)
    return saying


def main():
    with open('first_halves.txt', encoding='utf-8') as f:
        first_halves = f.read().split('\n')
    with open('second_halves.txt', encoding='utf-8') as f:
        second_halves = f.read()
        second_halves = second_halves.split('\n')
    saying = 'Яблоко от яблони недалеко падает'
    while saying in originals:
        saying = clean_output(generator(first_halves, second_halves))
    print(saying + '.')


if __name__ == '__main__':
    main()
