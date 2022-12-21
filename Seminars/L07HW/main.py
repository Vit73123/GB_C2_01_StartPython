import user_interface as ui


while(True):
    print("1 -> Создать запись")
    print("2 -> Сохранть запись в строчном формате")
    print("3 -> Сохранть запись в блочном формате")
    print("4 -> Просмотреть книгу в строчном формате")
    print("5 -> Просмотреть книгу в блочном формате")
    print("0 -> Выход")
    selector = int(input("Ваш выбор? "))
    if selector == 1:
        ui.button_input_click()
    elif selector == 2:
        ui.button_note1_save_click()
    elif selector == 3:
        ui.button_note2_save_click()
    elif selector == 4:
        ui.button_note1_view_all_click()
    elif selector == 5:
        ui.button_note2_view_all_click()
    elif selector == 0:
        ui.button_exit_click()