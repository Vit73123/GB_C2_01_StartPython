def loger(primer, result):
    with open('FirstProject/file.txt', 'a') as data:
        rasparse = "".join(map(str, primer))
        rasparse = rasparse + " = "
        result = str(result) + ';\n'
        data.write(str(rasparse))
        data.write(str(result))