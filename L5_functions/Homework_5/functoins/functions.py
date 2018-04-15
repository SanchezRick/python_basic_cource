import os


def card_has_errors(card_number):
    has_error = True
    card_list = card_number.split(" ")
    list_len = 4
    try:
        os.environ["region"] == "China"
        list_len = 3
    except:
        pass
    if len(card_list) != list_len:
        return has_error
    for i in card_list:
        try:
            value = int(i)
        except ValueError:
            return has_error
        else:
            if value < 0:
                return has_error
            if len(i) != 4:
                return has_error


def print_bank(card_number):
    card_list = card_number.split(" ")
    if card_list[0] == "5167":
        print("You use PrivatBank credit card")
        return
    if card_list[0] == "5375":
        print("You use Monobank credit card")
        return
    else:
        print("You use credit card from the unknown bank")
        return


def mm_yy_has_errors(mm_yy):
    has_error = True
    mm_yy_list = mm_yy.split("/")
    for i in mm_yy_list:
        try:
            value = int(i)
        except ValueError:
            return has_error
        else:
            mm = int(mm_yy_list[0])
            yy = int(mm_yy_list[1])
            if mm <= 12 and yy <= 99 and mm > 0 and yy >= 18:  # Проверка, месяц не больше 12, год не больше 99
                print('OK!')
                return
            else:
                return has_error


def cvv_has_errors(cvv_card):
    has_error = True
    len_cvv = 3
    for i in cvv_card:
        try:
            value = int(i)
        except ValueError:
            return has_error
    if len(cvv_card) == len_cvv:
        print(len(cvv_card))
        return
    else:
        return has_error