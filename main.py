import re

points_en = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}

points_ru = {"а": 1, "б": 3, "в": 1, "г": 3, "д": 2, "е": 1,
             "ё": 3, "ж": 5, "з": 5, "и": 1, "й": 4, "к": 2,
             "л": 2, "м": 2, "н": 1, "о": 1, "п": 2, "р": 1,
             "с": 1, "т": 1, "у": 2, "ф": 10, "х": 5, "ц": 5,
             "ч": 5, "ш": 8, "щ": 10, "ъ": 4, "ы": 4, "ь": 3, "э": 8,
             "ю": 8, "я": 3}

word = input("Введите слово: ").lower()
isCyrillic = bool(re.search('[а-я]', word))

if isCyrillic:
    total = 0
    for letter in word:
        total += points_ru[letter]
else:
    total = 0
    for letter in word:
        total += points_en[letter]

print(total)
