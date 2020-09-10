age = int(input())
def who_is_user(age):
    if age <= 7:
        return "Пользователь воспитанник детсада"
    elif 7 <= age <= 18:
        return "Пользователь - школьник"
    elif 18 <= age <= 23:
        return "Пользователь - студент ВУЗа"
    else:
        return "Пользователь работает"
    
print(who_is_user(40))