import re


def encryption(message, key, lang):
    result = ''
    if lang == 'ru':
        ru_low = [i for i in "абвгдежзийклмнопрстуфхцчшщъыьэюя"]
        ru_up = [i for i in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"]
        for letter in message:
            if letter in ru_low:
                result += ru_low[(ru_low.index(letter) + key) % 32]
            elif letter in ru_up:
                result += ru_up[(ru_up.index(letter) + key) % 32]
            else:
                result += letter
    else:
        for letter in message:
            if bool(re.search('[A-Z]', letter)):
                result += chr((ord(letter) + key - 65) % 26 + 65)
            elif bool(re.search('[a-z]', letter)):
                result += chr((ord(letter) + key - 97) % 26 + 97)
            else:
                result += letter
    return result


def decryption(message, key, lang):
    result = ''
    if lang == 'ru':
        ru_low = [i for i in "абвгдежзийклмнопрстуфхцчшщъыьэюя"]
        ru_up = [i for i in "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"]
        for letter in message:
            if letter in ru_low:
                result += ru_low[(ru_low.index(letter) - key) % 32]
            elif letter in ru_up:
                result += ru_up[(ru_up.index(letter) - key) % 32]
            else:
                result += letter
    else:
        eng_low = [i for i in "abcdefghijklmnopqrstuvwxyz"]
        eng_up = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        for letter in message:
            if letter in eng_low:
                result += eng_low[(eng_low.index(letter) - key) % 26]
            elif letter in eng_up:
                result += eng_up[(eng_up.index(letter) - key) % 26]
            else:
                result += letter
    return result


def mes_check(a):
    if bool(re.search('[а-яА-Я]', a)) or bool(re.search('[a-zA-Z]', a)):
        '''
        ru = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        eng_count = 0
        ru_count = 0
        for j in ru:
            ru_count += a.lower().count(j)
        for j in range(97, 123):
            eng_count += a.lower().count(chr(j))
        if eng_count != 0 and ru_count == 0:
            return a, 'eng'
        elif eng_count == 0 and ru_count != 0:
            return a, 'ru'
        else:
            return mes_check(input("Your message is mix of Russian letters and English\nPlease, try again: "))
        '''
        return a
    return mes_check(input("Your message is empty or it doesn't consist of Russian or English characters"
                           "\nPlease, try again: "))


def req_check(a):
    if a == "+" or a == "-":
        return a
    return req_check(input("Incorrect input\nWhat do I need to do:\n\tEncrypt: +\n\tDecrypt: -\nRequest: "))


def lang_check(a):
    if a == 'ru' or a == 'eng':
        return a
    return lang_check(input("Incorrect input.\nPlease, try again: "))


def cont_check(a):
    if a.lower() == 'yes' or a.lower() == 'no':
        return a
    return cont_check(input("Incorrect input\nPlease, try again: "))


def main():
    # message, mes_lang = mes_check(input("Message for encrypting: ")) # Two arguments for practising in multi-returning

    message = mes_check(input("Message for encrypting/decrypting: "))
    rot = int(input("Key for shifting right: "))
    language = lang_check(input("Please, write language of your message: "))
    request = input("What do I need to do:\n\tEncrypt: +\n\tDecrypt: -\nRequest: ")
    if request == '+':
        print(encryption(message, rot, language))
    elif request == '-':
        print(decryption(message, rot, language))
    '''
    for i in range(0, 27):
        print(decryption(message, i, language)) # Brute force decryption
    '''
    if cont_check(input("Would you like try it again? (yes/no)\nAnswer: ")) == 'yes':
        main()
    else:
        print("Have a nice day!")


main()
