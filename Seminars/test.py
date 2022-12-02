lst = ["qwe",	"asd",	"zxc", "qwe", "ertqwe"]
inString = input("Введите строку поиска: ")
count = 0
index = 0
for l in lst:
    if inString == l:
        count += 1
        if count == 2:
            break
    index += 1

if count == 2:
    print(index)
else:
    print(-1)
