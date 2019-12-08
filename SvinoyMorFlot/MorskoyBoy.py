import random

class half_of_ship():

    def __init__(self, symb, x, y):
        self.symb = symb
        self.x = x
        self.y = y

class ship():
    # Схип, ёпта
    def __init__(self, paluba):
        self.paluba = paluba

test = half_of_ship("2", 2, 2)

def show_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # ВНИМАНИЕ КОСТЫЛЬ ВНИМАНИЕ
            if type(matrix[i][j]) == type(test):
                # ВНИМАНИЕ КОСТЫЛЬ ВНИМАНИЕ
                print(matrix[i][j].symb, end=' ')
            else:
                print(matrix[i][j], end=' ')
        print()

def zer_matrix(matrix):
    for i in range(10):
        new_matr = []
        for j in range(10):
            new_matr.append("~")
        matrix.append(new_matr)

def ship_enter(matrix):
    x = int(input("Введите x: ")) - 1
    y = int(input("Введите y: ")) - 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i == x) and (j == y):
                matrix[i][j] = half_of_ship("◘",x ,y)
    return x, y

def enter_ship(trys, vector, matrix):
    ships = []
    x, y = ship_enter(matrix)
    ships.append(matrix[x][y])
    for elem in range(trys - 1):
        if vector == "up":
            x -= 1
            matrix[x][y] = half_of_ship("◘",x ,y)
            ships.append(matrix[x][y])
        elif vector == "down":
            x += 1
            matrix[x][y] = half_of_ship("◘", x, y)
            ships.append(matrix[x][y])
        elif vector == "left":
            y -= 1
            matrix[x][y] = half_of_ship("◘", x, y)
            ships.append(matrix[x][y])
        elif vector == "right":
            y += 1
            matrix[x][y] = half_of_ship("◘", x, y)
            ships.append(matrix[x][y])

    return ships

def shoot(matrix):
    x = int(input("Введите x: ")) - 1
    y = int(input("Введите y: ")) - 1

    if type(matrix[x][y]) == type(test):
        matrix[x][y] = 'X'
        show_matrix(matrix)
        # if check(matrix) == False:
        #     shoot(matrix)
        # else:
        #     print ('GG')
    else:
        matrix[x][y] = "0"
        show_matrix(matrix)

def check (matrix):
    zero = True
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if type(matrix[i][j]) == type(test):
                zero = False
    if zero == False:
        shoot(matrix)
    else:
        print('GG')

    return zero


def play(player_one, player_two):
    player = random.randint(1, 2)

    if player == 1:
        print('Игрок', player, 'ходит')
        while True:
            shoot(player_two)
            if check(player_two) == True:
                break
            shoot(player_one)
            if check(player_one) == True:
                break
    elif player == 2:
        print('Игрок', player, 'ходит')
        while True:
            shoot(player_one)
            if check(player_one) == True:
                break
            shoot(player_two)
            if check(player_two) == True:
                break



#MAIN#

player_one = []
player_two = []


zer_matrix(player_one)
show_matrix(player_one)
#f - первый игрок; o/t/th/f - первый, второй, третий, четвёртый по счёту корабль; o/t/th/f - однно\дву\трёх\четырёх палубный корабль
f_o_o_ship = enter_ship(1, "up", player_one)
show_matrix(player_one)
# f_o_t_ship = enter_ship(2, input("Введите направление "), player_one)
# show_matrix(player_one)
# f_o_th_ship = enter_ship(3, input("Введите направление "), player_one)
# show_matrix(player_one)
# f_o_f_ship = enter_ship(4, input("Введите направление "), player_one)
# show_matrix(player_one)
# s - второй игрок; o/t/th/f - первый, второй, третий, четвёртый по счёту корабль; o/t/th/f - однно\дву\трёх\четырёх палубный корабль
zer_matrix(player_two)
show_matrix(player_two)

print

s_o_o_ship = enter_ship(1, "up", player_two)
show_matrix(player_two)
# s_o_t_ship = enter_ship(2, input("Введите направление "), player_two)
# show_matrix(player_two)
# s_o_th_ship = enter_ship(3, input("Введите направление "), player_two)
# show_matrix(player_two)
# s_o_f_ship = enter_ship(4, input("Введите направление "), player_two)
# show_matrix(player_two)
play(player_one, player_two)
shoot(player_one)