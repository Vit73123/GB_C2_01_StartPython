import note1
import note2

data = ('a1', 'b', 'c', 'd')
all_data = []

def init():
    global data
    data =  (input('Фамилия : '),
             input('Имя     : '),
             input('Телефон : '),
             input('Описание: '))

def get():
    return data

def get_all_note1():
    set_all_note1()
    return all_data

def set_all_note1():
    global all_data
    all_data = note1.get_all()

def get_all_note2():
    set_all_note2()
    return all_data

def set_all_note2():
    global all_data
    all_data = note2.get_all()

def save_note1():
    note1.save(data)

def save_note2():
    note2.save(data)