import random       # нужна для генрации поля


def nach():         # функция для определения уровня сложности
    global a, slog
    print('Выберите уровень сложности: "-1" - легчайший, '
          '"0" - простой, "1" - средний, "2" - сложный')
    slog = int(input())
    if slog == -1 or slog == 0:
        a = 5
    elif slog == 1:
        a = 9
    elif slog == 2:
        a = 16
    else:
        print('вы ввели некорректное значение')
        nach()


def print_pol():               # функция для визуализации поля
    global pol, n
    print()
    n = 0
    for i in pol:
        for j in i:
            if j == []:
                print('[ ]', end=' ')
                n += 1
            elif isinstance(j, int):
                print(' ', j, sep='', end='  ')
            elif j[0] == 'F':
                print('[F]', end=' ')
                n += 1
            elif j[0] == '?':
                print('[?]', end=' ')
                n += 1
            elif j == [' ']:
                print('  ', end='  ')
            elif j == ['m']:
                print('[ ]', end=' ')
                n += 1
            else:
                print('[ ]', end=' ')
                n += 1
        print()


def hod(hodp=[]):                    # функция для приёма хода игрока
    print()
    print('Задайте ваш ход при помощи указания через пробел '
          'сначал номера выбранной строки, а потом столбца')
    print('(номерация начинается с 1 и идёт сверху '
          'вниз и слева на право)')
    print('Так же вы можете указать специальное действие'
          '(тоже через пробел): поставить флаг - "f" и поставить вопрос - "?"')
    hodp = input().split()
    if len(hodp) > 3 or len(hodp) < 2:
        print('Некорректное указание хода')
        return (hod(hodp))
    elif (not isinstance(int(hodp[0]), int)) or (not isinstance(int(hodp[1]), int)):
        print('Номера строки и столбца должны быть числами')
        return (hod(hodp))
    elif int(hodp[0]) < 1 or int(hodp[1]) < 1 or int(hodp[0]) > a or int(hodp[1]) > a:
        print('Вы указали координаты за пределами игрового поля')
        return (hod(hodp))
    elif len(hodp) == 3 and hodp[2] != 'f' and hodp[2] != '?':
        print('Неверное указание действия')
        return (hod(hodp))
    else:
        return (hodp)


def open(x, y, fl=True):                 # функция для открытия клеток поля
    global pol
    if pol[x][y] == []:
        pol[x][y] = [' ']
        if fl:
            if x > 0 and x < a - 1 and y > 0 and y < a - 1:
                open(x - 1, y - 1)
                open(x - 1, y)
                open(x - 1, y + 1)
                open(x, y - 1)
                open(x, y + 1)
                open(x + 1, y - 1)
                open(x + 1, y)
                open(x + 1, y + 1)
            elif x > 0 and x < a - 1 and y == 0:
                open(x - 1, y)
                open(x - 1, y + 1)
                open(x, y + 1)
                open(x + 1, y)
                open(x + 1, y + 1)
            elif x > 0 and x < a - 1 and y == a - 1:
                open(x - 1, y - 1)
                open(x - 1, y)
                open(x, y - 1)
                open(x + 1, y - 1)
                open(x + 1, y)
            elif x == 0 and y > 0 and y < a - 1:
                open(x, y - 1)
                open(x, y + 1)
                open(x + 1, y - 1)
                open(x + 1, y)
                open(x + 1, y + 1)
            elif x == 0 and y == 0:
                open(x, y + 1)
                open(x + 1, y)
                open(x + 1, y + 1)
            elif x == 0 and y == a - 1:
                open(x, y - 1)
                open(x + 1, y - 1)
                open(x + 1, y)
            elif x == a - 1 and y > 0 and y < a - 1:
                open(x - 1, y - 1)
                open(x - 1, y)
                open(x - 1, y + 1)
                open(x, y - 1)
                open(x, y + 1)
            elif x == a - 1 and y == 0:
                open(x - 1, y)
                open(x - 1, y + 1)
                open(x, y + 1)
            elif x == a - 1 and y == a - 1:
                open(x - 1, y - 1)
                open(x - 1, y)
                open(x, y - 1)
    elif pol[x][y] != [] and pol[x][y] != [' '] and pol[x][y] != ['m'] \
            and not isinstance(pol[x][y], int):
        pol[x][y] = pol[x][y][0]


nach()
pol = [[[]] * a for _ in range(a)]
if slog == -1:
    mi = 0
elif slog == 0:
    mi = 3
elif slog == 1:
    mi = 10
elif slog == 2:
    mi = 40
mins = mi
while mi > 0:               # генерация мин на поле
    x = random.randint(0, a - 1)
    y = random.randint(0, a - 1)
    if pol[x][y] != ['m'] and pol[x][y] != [' ']:
        mi -= 1
        pol[x][y] = ['m']
print_pol()
dey = hod()                    # первый ход игрока(защищённый)
if len(dey) == 2:
    if pol[int(dey[0]) - 1][int(dey[1]) - 1] != ['m']:
        open(int(dey[0]) - 1, int(dey[1]) - 1, False)
    elif pol[int(dey[0]) - 1][int(dey[1]) - 1] == []:
        open(int(dey[0]) - 1, int(dey[1]) - 1)
    else:
        mi = 1
        while mi > 0:
            x = random.randint(0, a - 1)
            y = random.randint(0, a - 1)
            if pol[x][y] != ['m'] and pol[x][y] != [' ']:
                mi -= 1
                pol[x][y] = ['m']
        print(' mine ')
        pol[int(dey[0]) - 1][int(dey[1]) - 1] = []
        open(int(dey[0]) - 1, int(dey[1]) - 1)
else:
    if pol[int(dey[0]) - 1][int(dey[1]) - 1] != []:
        if dey[2] == 'f' and pol[int(dey[0]) - 1][int(dey[1]) - 1][0] != 'F':
            pol[int(dey[0]) - 1][int(dey[1]) - 1].insert(0, 'F')
        elif dey[2] == 'f' and pol[int(dey[0]) - 1][int(dey[1]) - 1][0] == 'F':
            pol[int(dey[0]) - 1][int(dey[1]) - 1].pop(0)
        elif dey[2] == '?' and pol[int(dey[0]) - 1][int(dey[1]) - 1][0] != '?':
            pol[int(dey[0]) - 1][int(dey[1]) - 1].insert(0, '?')
        elif dey[2] == '?' and pol[int(dey[0]) - 1][int(dey[1]) - 1][0] == '?':
            pol[int(dey[0]) - 1][int(dey[1]) - 1].pop(0)
    else:
        if dey[2] == 'f' and pol[int(dey[0]) - 1][int(dey[1]) - 1] != ['F']:
            pol[int(dey[0]) - 1][int(dey[1]) - 1].append('F')
        elif dey[2] == 'f' and pol[int(dey[0]) - 1][int(dey[1]) - 1] == ['F']:
            pol[int(dey[0]) - 1][int(dey[1]) - 1] = []
        elif dey[2] == '?' and pol[int(dey[0]) - 1][int(dey[1]) - 1] != ['?']:
            pol[int(dey[0]) - 1][int(dey[1]) - 1].append('?')
        elif dey[2] == '?' and pol[int(dey[0]) - 1][int(dey[1]) - 1] == ['?']:
            pol[int(dey[0]) - 1][int(dey[1]) - 1] = []
for i in range(len(pol)):
    for j in range(len(pol[i])):
        n = 0
        if pol[i][j] != ['m']:
            if i > 0 and i < a - 1 and j > 0 and j < a - 1:
                if ['m'] in pol[i - 1][j - 1:j + 2]:
                    n += pol[i - 1][j - 1:j + 2].count(['m'])
                if ['m'] in pol[i][j - 1:j + 2]:
                    n += pol[i][j - 1:j + 2].count(['m'])
                if ['m'] in pol[i + 1][j - 1:j + 2]:
                    n += pol[i + 1][j - 1:j + 2].count(['m'])
            elif i > 0 and i < a - 1 and j == 0:
                if ['m'] in pol[i - 1][j:j + 2]:
                    n += pol[i - 1][j:j + 2].count(['m'])
                if ['m'] in pol[i][j:j + 2]:
                    n += pol[i][j:j + 2].count(['m'])
                if ['m'] in pol[i + 1][j:j + 2]:
                    n += pol[i + 1][j:j + 2].count(['m'])
            elif i > 0 and i < a - 1 and j == a - 1:
                if ['m'] in pol[i - 1][j - 1:j + 1]:
                    n += pol[i - 1][j - 1:j + 1].count(['m'])
                if ['m'] in pol[i][j - 1:j + 1]:
                    n += pol[i][j - 1:j + 1].count(['m'])
                if ['m'] in pol[i + 1][j - 1:j + 1]:
                    n += pol[i + 1][j - 1:j + 1].count(['m'])
            elif i == 0 and j > 0 and j < a - 1:
                if ['m'] in pol[i][j - 1:j + 2]:
                    n += pol[i][j - 1:j + 2].count(['m'])
                if ['m'] in pol[i + 1][j - 1:j + 2]:
                    n += pol[i + 1][j - 1:j + 2].count(['m'])
            elif i == 0 and j == 0:
                if ['m'] in pol[i][j:j + 2]:
                    n += pol[i][j:j + 2].count(['m'])
                if ['m'] in pol[i + 1][j:j + 2]:
                    n += pol[i + 1][j:j + 2].count(['m'])
            elif i == 0 and j == a - 1:
                if ['m'] in pol[i][j - 1:j + 1]:
                    n += pol[i][j - 1:j + 1].count(['m'])
                if ['m'] in pol[i + 1][j - 1:j + 1]:
                    n += pol[i + 1][j - 1:j + 1].count(['m'])
            elif i == a - 1 and j > 0 and j < a - 1:
                if ['m'] in pol[i - 1][j - 1:j + 2]:
                    n += pol[i - 1][j - 1:j + 2].count(['m'])
                if ['m'] in pol[i][j - 1:j + 2]:
                    n += pol[i][j - 1:j + 2].count(['m'])
            elif i == a - 1 and j == 0:
                if ['m'] in pol[i - 1][j:j + 2]:
                    n += pol[i - 1][j:j + 2].count(['m'])
                if ['m'] in pol[i][j:j + 2]:
                    n += pol[i][j:j + 2].count(['m'])
            elif i == a - 1 and j == a - 1:
                if ['m'] in pol[i - 1][j - 1:j + 1]:
                    n += pol[i - 1][j - 1:j + 1].count(['m'])
                if ['m'] in pol[i][j - 1:j + 1]:
                    n += pol[i][j - 1:j + 1].count(['m'])
        if n != 0:
            pol[i][j] = [n]
if len(dey) == 2:
    open(int(dey[0]) - 1, int(dey[1]) - 1, False)
print_pol()
flag = True
while flag:      # сам игровой процесс
    dey = hod()
    if len(dey) == 2:
        if pol[int(dey[0]) - 1][int(dey[1]) - 1] != ['m']:
            open(int(dey[0]) - 1, int(dey[1]) - 1)
        else:
            print('Тут была мины. Вы проиграли...')            # проигрыш
            flag = False
            break
    else:
        if pol[int(dey[0]) - 1][int(dey[1]) - 1] != []:
            if dey[2] == 'f' and pol[int(dey[0]) - 1][int(dey[1]) - 1][0] != 'F':
                pol[int(dey[0]) - 1][int(dey[1]) - 1].insert(0, 'F')
            elif dey[2] == 'f' and pol[int(dey[0]) - 1][int(dey[1]) - 1][0] == 'F':
                pol[int(dey[0]) - 1][int(dey[1]) - 1].pop(0)
            elif dey[2] == '?' and pol[int(dey[0]) - 1][int(dey[1]) - 1][0] != '?':
                pol[int(dey[0]) - 1][int(dey[1]) - 1].insert(0, '?')
            elif dey[2] == '?' and pol[int(dey[0]) - 1][int(dey[1]) - 1][0] == '?':
                pol[int(dey[0]) - 1][int(dey[1]) - 1].pop(0)
        else:
            if dey[2] == 'f' and pol[int(dey[0]) - 1][int(dey[1]) - 1] != ['F']:
                pol[int(dey[0]) - 1][int(dey[1]) - 1].append('F')
            elif dey[2] == 'f' and pol[int(dey[0]) - 1][int(dey[1]) - 1] == ['F']:
                pol[int(dey[0]) - 1][int(dey[1]) - 1] = []
            elif dey[2] == '?' and pol[int(dey[0]) - 1][int(dey[1]) - 1] != ['?']:
                pol[int(dey[0]) - 1][int(dey[1]) - 1].append('?')
            elif dey[2] == '?' and pol[int(dey[0]) - 1][int(dey[1]) - 1] == ['?']:
                pol[int(dey[0]) - 1][int(dey[1]) - 1] = []
    print_pol()
    if mins == n:           # победа
        print('Победа')
        flag = False
        break