# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# 2021 21 ---> 2000 бот4 -> 1996 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# *** Дополнительно: ***
# b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!! Не моё решение задачи. Я не решал задачу (некогда) !!!
# !!!        Это готовое решение преподавателя           !!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from random import *
import os

def player_vs_player():
    candies_total = 120
    max_take = 28
    count = 0
    player_1 = input("Ваше имя?: ")
    player_2 = input("Имя соперника?: ")

    print("Первым будет ходить...")

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f"Поздравляю {lucky}, ты ходишь первым!")

    while candies_total > 0:
        if count == 0:
            step = int(input(f"Сколько же вы возьмёте {lucky} = "))
            while step > candies_total or step > max_take:
                step = int(input(f"Можно взять не больше {max_take} конфет {lucky}, попробуй ещё раз: "))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f"на кону ещё {candies_total}")
            count = 1
        else:
            print("Конец игры")

        if count == 1:
            step = int(input(f"Сколько же вы возьмёте {loser} = "))
            while step > candies_total or step > max_take:
                step = int(input(f"Можно взять не больше {max_take} конфет {lucky}, попробуй ещё раз: "))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f"\nна кону ещё {candies_total}")
            count = 0
        else:
            print("Конец игры")

    if count == 1:
        print(f"{loser} победил!")
    if count == 0:
        print(f"{lucky} победил!")

player_vs_player()