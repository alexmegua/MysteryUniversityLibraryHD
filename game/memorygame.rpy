init python:
    import random

    def reset_game():
        global cards, revealed, first_card, second_card, waiting_for_second_card, pairs_found
        cards = ["A", "A", "B", "B", "C", "C", "D", "D"]
        random.shuffle(cards)
        revealed = [False] * len(cards)
        first_card = None
        second_card = None
        waiting_for_second_card = False
        pairs_found = 0  # Initialize pairs_found

    reset_game()

    def check_match():
        if first_card is not None and second_card is not None:
            return cards[first_card] == cards[second_card]
        return False

    def reveal_card(index):
        global first_card, second_card, waiting_for_second_card

        if revealed[index] or waiting_for_second_card:
            return

        revealed[index] = True

        if first_card is None:
            first_card = index
        else:
            second_card = index
            waiting_for_second_card = True
            renpy.invoke_in_new_context(check_and_reset)  # Вызов в новом контексте

    def check_and_reset():
        global first_card, second_card, waiting_for_second_card, pairs_found

        renpy.pause(0.5)  # Задержка перед проверкой

        if check_match():
            pairs_found += 1
            # Добавляем сообщения для разных типов карт
            messages = {
                "A": "Будівля на вулиці 68-ї десантної бригади — серце університету. Тут починався шлях багатьох науковців.",
                "B": "Перший герб згорів у пожежі 1904-го. Але форма залишилася як символ стійкості та відродження.",
                "C": "Петро Могила був видатним освітянином та релігійним діячем. Його ім’я об’єднує університет з традицією гуманістичної освіти.",
                "D": "Кіт Сін — неофіційний талісман університету. Кажуть, він слухав більше лекцій, ніж дехто зі студентів."
            }
            renpy.say(None, messages[cards[first_card]])  # Показываем сообщение
        else:
            revealed[first_card] = False
            revealed[second_card] = False

        first_card = None
        second_card = None
        waiting_for_second_card = False

screen memory_game_screen:
    grid 4 2:
        spacing 25
        align (0.5, 0.5)

        for i in range(len(cards)):
            imagebutton:
                idle ConditionSwitch(
                    "revealed[{}]".format(i), "images/card_{}.png".format(cards[i]),
                    "True", "images/card_question.png"
                )
                action Function(reveal_card, i)
                sensitive (not revealed[i]) and (not waiting_for_second_card)
                at card_transform

transform card_transform:
    size (150, 200)
    zoom 0.8

label MemoryGame:
    scene bg8
    stop music 
    show screen memory_game_screen
    play music "audio/puzzlemusic.wav" fadein 5.0
    while not all(revealed):
        $ renpy.pause(0.01)  # Пауза, пока не будут открыты все карты

    hide screen memory_game_screen
    "Ви знайшли всі пари!"
    
    # Скрываем все элементы, связанные с игрой
    hide screen memory_game_screen
    stop music fadeout 1.0  # Останавливаем музыку

    return