import os
import re

def name_has_errors(name_surname):
    has_errors = re.match(r'^[a-zA-Z]+\ [a-zA-Z]+$', name_surname)
    if has_errors:
        return True


def card_has_errors(card_number):
    card_errors = re.match(r'(^[0-9]{4}\ [0-9]{4}\ [0-9]{4}\ [0-9]{4}$)', card_number)
    if card_errors:
        return True

def print_bank(card_number):
    if card_number.startswith("5167"):
        print("You use PrivatBank credit card")
        return
    if card_number.startswith("5375"):
        print("You use Monobank credit card")
        return
    else:
        print("You use credit card from the unknown bank")
        return


def mm_yy_has_errors(mm_yy):
    mm_yy_errors = re.match(r'(^[0-9]{2}\/[0-9]{2}$)', mm_yy)
    mm_yy_list = mm_yy.split("/")
    if mm_yy_errors and int(mm_yy_list[0]) and int(mm_yy_list[1]) and int(mm_yy_list[0]) <= 12 and int(mm_yy_list[1]) <= 99 and int(mm_yy_list[0])  > 0 and int(mm_yy_list[1]) >= 18:
        return True


def cvv_has_errors(cvv_card):
    cvv_errors = re.match(r'^[0-9]{3}$', cvv_card)
    if cvv_errors:
        return True