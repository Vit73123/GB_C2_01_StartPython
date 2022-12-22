EOL = '\n'

def save(data):
    with open('note_2_data', 'a') as db:
        db.write(set_block(data))

def get_all():
    data = []
    line = []
    with open('note_2_data', 'r') as db:
        for l in db:
            if eol(l):
                data.append(line)
                line = []
            else:
                line.append(l[:-1])
    return data

def set_block(data):
    return '\n'.join(data) + '\n' + EOL

def eol(line):
    return (line == EOL)