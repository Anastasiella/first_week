def asking():
    try:
        while True:
            ask_user = input('Как дела? ')
            if ask_user == 'Хорошо':
                print('Отлично')
                break
    except KeyboardInterrupt:
        print("\nПока!")
asking()