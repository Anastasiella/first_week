my_answers = {"Как дела?": "Хорошо!", "Что делаешь?":"Программирую", "Когда на работу пойдешь?":"Когда рак на горе свиснет"}
def asking():
    stop_word = "Пока"
    ask_user = None
    while ask_user != stop_word:
        ask_user = input('Как дела? ')
        if ask_user == 'Хорошо':
            print('Отлично')
            break
        elif ask_user in my_answers.keys():
            print(my_answers.get(ask_user))
        elif ask_user == stop_word:
            print("Ну пока")
            break
        else:
            print("Давай поговорим еще")
asking()