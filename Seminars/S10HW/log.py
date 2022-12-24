def loger(primer, result, user_id, user_name):
    with open('file.txt', 'a') as data:
        rasparse = "".join(map(str, primer))
        rasparse = rasparse + " = "
        result = str(result) + ' ' + str(user_id) + ' ' + str(user_name) + ';\n'
        data.write(str(rasparse))
        data.write(str(result))