from random import choice


def check_answer(a):
    if a.isalpha():
        if a.lower() == 'да' or a.lower() == 'нет':
            return a
        print("Ты ввёл некорректные данные")
        return check_answer(input("Хочешь задать ещё вопрос? (да, нет)\n"))
    print("Ты ввёл некорректные данные")
    return check_answer(input("Хочешь задать ещё вопрос? (да, нет)\n"))


answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
           "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
           "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять",
           "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]

print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input("Введите Ваше имя: ")
print("Привет,", name)

while True:
    input("Какой у тебя вопрос?\n")
    print(choice(answers))
    if check_answer(input("Хочешь задать ещё вопрос? (да, нет)\n")) != 'да':
        break