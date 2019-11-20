

def password_validation(pasw):
    """
    passw - строка
    Проверяется на длинну и наличие цифр и букв
    :return: {'ok':bool}
    """
    if len(pasw) < 6:
        return False, 'Пароль должен быть длиннее 5 символов'
    if pasw.isdigit() or pasw.isalpha():
        return False, 'В пароле должны быть и буквы и цифры'
    return True, 'Ok'