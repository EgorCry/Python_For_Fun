from random import choice

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."
chars = ''


def generate_password(length, available_chars):
    password = ''
    for _ in range(length):
        password += choice(available_chars)
    return password


def int_input(a):
    if a.isdigit():
        return int(a)
    return int_input(input("Вы ввели некорректные данные. Попробуйте ещё раз: "))


def answer_input(a):
    if a.isalpha():
        if a.lower() == "да" or a.lower() == "нет":
            return a
        return answer_input(input("Вы ввели некорректные данные. Попробуйте ещё раз: "))
    return answer_input(input("Вы ввели некорректные данные. Попробуйте ещё раз: "))


passwords_quantity = int_input(input("Сколько паролей сгенерировать?\n"))

password_length = int_input(input("Сколько символов должно быть в пароле?\n"))

digits_access = answer_input(input("Нужны ли символы: 0123456789? (да, нет)\n"))
chars += (digits_access == 'да' and digits or '')

uppercase_access = answer_input(input("Нужны ли прописные буквы: ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да, нет)\n"))
chars += (uppercase_access == 'да' and uppercase_letters or '')

lowercase_access = answer_input(input("Нужны ли строчные буквы: abcdefghijklmnopqrstuvwxyz? (да, нет)\n"))
chars += (lowercase_access == 'да' and lowercase_letters or '')

punctuation_access = answer_input(input("Нужны ли следующие символы: !#$%&*+-=?@^_.? (да, нет)\n"))
chars += (punctuation_access == 'да' and punctuation or '')

ambiguity_access = answer_input(input("Нужны ли неоднозначные символы: il1Lo0O? (да, нет)\n"))
if ambiguity_access == 'нет':
    for i in "il1Lo0O":
        if i in chars:
            chars = chars.replace(i, '')


passwords = []
for _ in range(passwords_quantity):
    passwords.append(generate_password(password_length, chars))

print(*passwords, sep="\n")