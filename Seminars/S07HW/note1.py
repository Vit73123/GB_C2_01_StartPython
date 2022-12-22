def save(data):
    with open('note_1_data', 'a') as db:
        db.write(set_line(data))

def get_all():
    data = []
    with open('note_1_data', 'r') as db:
        for line in db:
            data.append(tuple(line[:-1].split(',')))
    return data

def set_line(data):
    return ','.join(data) + '\n'