import phone

def button_input_click():
    phone.init()

def button_note1_save_click():
    phone.save_note1()

def button_note2_save_click():
    phone.save_note2()
    
def button_note1_view_all_click():
    view_all(phone.get_all_note1())

def button_note2_view_all_click():
    view_all(phone.get_all_note2())

def button_exit_click():
    exit()

def view_all(all_data):
    for line in all_data:
        print(line)