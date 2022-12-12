# 1) Вычислить число Pi c заданной точностью d, не используя ф. round()

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


import math

def roundFNum(num, prec):
    return float(int(num * 10 ** prec) / 10 ** prec)

PREC = int(input("Введите точность p (10 ^ -p): "))
STEP = int(input("Введите шаги итераций       : "))
i = 0
s1 = 0.0
s2 = 0.0
index = 0
while True:
    index += 1
    i += 1
    s1 = s2 + 4 / (2 * i - 1)
    i += 1
    s2 = s1 - 4 / (2 * i - 1)
    if s1 - s2 < 10 ** (-PREC):
        break
    if index % STEP == 0:
        if input(f"{index} Pi = {roundFNum((s1 + s2) / 2, PREC)} Math.Pi = {roundFNum(math.pi, PREC)} \
            Достигнута точность: {s1 - s2} Закончить вычисления (x)? ") == 'x':
            break
print(f"Pi = {roundFNum((s1 + s2) / 2, PREC)} Итераций {index}")