stroka = 'a a b a c b d d c d'
list = stroka.split()
count = 1
list_2 = {}

for i in range(len(list)):
    if list[i] not in list_2.keys():
        list_2[list[i]] = 0
        print(f'{list[i]} ', end='')
    else:
        list_2[list[i]] += 1
        print(f'{list[i]}_{list_2[list[i]]} ', end='')
          
        