import re
# Файл для проверки корректности информации

def main_func(partner_data: dict):
    # Функция для общей проверки информации
    if (check_name(partner_data['name']) and
            check_phone(partner_data['phone']) and
            check_mail(partner_data['mail']) and
            check_inn(partner_data['inn']) and
            check_type(partner_data['type']) and
            check_dir_name(partner_data['director']) and
            check_ur_addr(partner_data['ur_addr']) and
            check_rate(partner_data['rate'])):
        return True
    return False


def check_name(name):
    if len(name) != 0:
        return True
    return False


def check_phone(phone_number):
    try:
        regex = re.compile(r'[0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9] [0-9][0-9]')
        if re.fullmatch(regex, phone_number):
            return True
        return False
    except Exception:
        return False


def check_dir_name(dir_name):
    if len(dir_name.split(" ")) == 3:
        return True
    return False


def check_rate(rate):
    if int(rate) in range(1, 11):
        return True
    return False


def check_mail(mail_text):
    if (len(mail_text) != 0 and
            len(mail_text.split("@")) == 2 and
            len(mail_text.split("@")[1].split(".")) == 2):
        return True
    return False


def check_inn(inn: str):
    if len(inn) == 10 and inn.isdigit():
        return True
    return False


def check_ur_addr(ur_addr):
    if (len(ur_addr.split(", ")[0]) == 6 and ur_addr.split(", ")[0].isdigit()
            and len(ur_addr.split(", ")[1]) != 0):
        return True
    return False


def check_type(partner_type):
    if partner_type in ["ЗАО", "ООО", "ПАО", "ОАО"]:
        return True
    return False
