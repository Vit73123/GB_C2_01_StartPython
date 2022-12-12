# 2) Создайте программу для игры в ""Крестики-нолики"".

# Не моё решение задачи. Я не нешал задачу (некогда)
# Это готовое решение преподавателя.

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!! Не моё решение задачи. Я не решал задачу (некогда) !!!
# !!!        Это готовое решение преподавателя           !!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

board = list(range(1, 10))

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|",board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

["X", "0", "X", "", "X", "0", "", "", ""]

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод.")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in "X0"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Место занято")
        else:
            print("Некорректный ввод. Введите число от 1 до 9, чтобы сделать ход.")


def check_win(board):
    coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (8, 4, 8), (2, 4, 6))
    for c in coord:
        if board[c[0]] == board[c[1]] == board[c[2]]:
            return board[c[0]]
    return False

def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            take_input("X")
        else:
            take_input("0")
        count += 1
        if count > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "Выиграл!")
                win = True
                break
        if count == 0:
            print("Ничья!")
            break
    draw_board(board)

main(board)
