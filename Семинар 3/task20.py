n = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2:'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
if (n != 0) and (n != 1):
    print('Принимаются только два значения: 1 и 0')
else:
    word = input('Введите слово: ').upper()
    sum = 0
    if n == 1:
        for i in word:
            for k, v in points_en.items():
                if i in v:
                    sum += k 
    else:
        for i in word:
            for k, v in points_ru.items():
                if i in v:
                    sum += k 
    print(f'У вас {sum} очков')