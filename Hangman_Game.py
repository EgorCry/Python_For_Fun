import random


def get_word(language):
    if language.lower() == 'русский':
        with open('words_hangman_rus.txt', encoding='utf-8', mode='r') as file:
            word = random.choice(file.read().splitlines())
            file.close()
    elif language.lower() == 'english':
        with open('words_hangman.txt', 'r') as file:
            word = random.choice(file.read().splitlines())
            file.close()
    if word not in guessed_words:
        return word
    return get_word(language)


def lang_check(language):
    if language.lower() == 'русский' or language.lower() == 'english':
        return language
    return lang_check(input("Incorrect input! Try again, please!\nenglish or русский: "))


def display_hangman(tries):
    stage = [  # Final stage
        '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -''',
        # Pre-final stage: head, body, left hand, right hand, left leg
        '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / 
        -''',
        # Fourth stage: head, body, left hand, right hand
        '''
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |      
        -''',
        # Third stage: head, body, left hand
        '''
        --------
        |      |
        |      O
        |     \\|
        |      |
        |     
        -''',
        # Second stage: head, body
        '''
        --------
        |      |
        |      O
        |      |
        |      |
        |     
        -''',
        # First stage: head
        '''
        --------
        |      |
        |      O
        |    
        |      
        |     
        -''',
        # default
        '''
        --------
        |      |
        |      
        |    
        |      
        |     
        -'''
    ]
    return stage[tries]


def fool_check(a, lang, used_letters):
    if lang == 'english':
        if a.isalpha() and len(a) == 1:
            if a in used_letters:
                return fool_check(input('Letter was already used. Try another one: '), lang, used_letters)
            return a
        return fool_check(input('Invalid input. Try again: '), lang, used_letters)
    ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if a in ru and len(a) == 1:
        if a in used_letters:
            return fool_check(input('Letter was already used. Try another one: '), lang, used_letters)
        return a
    return fool_check(input('Invalid input. Try again: '), lang, used_letters)


def to_word(not_word):
    temp = ''
    for i in not_word:
        temp += i
    return temp


def fool_answer(a):
    if a.lower() == 'yes':
        return True
    if a.lower() == 'no':
        return False
    return fool_check(input('Invalid input. Try again: '))


def play():
    lang = lang_check(input("Which language do you prefer: русский or english?\nAnswer: "))
    word = get_word(lang)
    guessed_words.append(word)
    word_completion = '_' * len(word)
    guessed = False
    used_letters = list()
    tries = 6
    print("This is place for you, my lil' hangy", display_hangman(tries), f'\nYou have: {tries}', ('tries' if tries > 1
                                                                                                   else 'try'))
    while not guessed:
        print('Current word:', word_completion)
        try_word = fool_check(input('Your intended letter: '), lang, used_letters)
        used_letters.append(try_word)
        if try_word in word:
            word_completion = [i for i in word_completion]
            word = [i for i in word]
            for i in range(len(word)):
                if word[i] == try_word:
                    word_completion[i] = try_word
            word = to_word(word)
            word_completion = to_word(word_completion)
            print('Good choice!')
        else:
            tries -= 1
            print(display_hangman(tries))
            print(f'You have {tries}', ('tries' if tries > 1 else 'try'))
        if '_' not in word_completion:
            guessed = True
        if tries == 0:
            break
    if guessed:
        print('You\'ve won! Congratulations!!!')
    else:
        print(f'You\'ve lose... That\'s the word: {word}')
    print('Want to play again?')
    if fool_answer(input('Want to play again? (yes/no)\nAnswer: ')):
        play()
    else:
        print('Have a nice day!')


guessed_words = list()


print('Let\'s play a hangman game!')
play()
