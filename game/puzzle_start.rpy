default puzzle_solved = False

init python:
    import random
    import math

    correct_sentence = ["Минуле", "зберігає", "відповіді", "але", "вимагає", "плати"]

    def reset_puzzle():
        global shuffled_sentence, player_sentence, word_positions
        shuffled_sentence = correct_sentence[:]
        random.shuffle(shuffled_sentence)
        player_sentence = []

        word_positions = {}
        radius = 250  # радіус кола в пікселях (межі слів)
        center_x, center_y = 0.5, 0.4  # центр у відносних координатах
        min_dist = 130  # мінімальна відстань між словами

        placed_positions = []

        for word in shuffled_sentence:
            for attempt in range(100):
                angle = random.uniform(0, 2 * math.pi)
                r = random.uniform(0, radius)
                dx = math.cos(angle) * r
                dy = math.sin(angle) * r
                xpos = center_x + dx / config.screen_width
                ypos = center_y + dy / config.screen_height

                # перевірка на відстань
                too_close = False
                for px, py in placed_positions:
                    dist = math.hypot((xpos - px) * config.screen_width, (ypos - py) * config.screen_height)
                    if dist < min_dist:
                        too_close = True
                        break
                if not too_close:
                    word_positions[word] = (xpos, ypos)
                    placed_positions.append((xpos, ypos))
                    break

    reset_puzzle()

screen puzzle_minigame():

    tag minigame

    # Додаємо зображення відкритої книги перед усім іншим
    add "gui/book_open.png"  at Transform(zoom=1.75) xalign 0.5 yalign 0.5

    # Заголовок
    frame:
        xalign 0.5
        yalign 0.05
        has vbox
        text "Склади речення:" size 30

    # Слова навколо центру
    for word in shuffled_sentence:
        if word not in player_sentence:
            $ xpos, ypos = word_positions[word]
            textbutton word:
                xalign xpos
                yalign ypos
                action Function(player_sentence.append, word)
                style "button"

    # Область для зібраного речення (тільки якщо є хоча б 1 слово)
    if player_sentence:
        frame:
            xalign 0.5
            yalign 0.1
            has hbox spacing 10

            for word in player_sentence:
                textbutton word:
                    action Function(player_sentence.remove, word)

    # Кнопка перевірки
    frame:
        xalign 0.5
        yalign 0.93
        has vbox
        textbutton "Перевірити":
            action Return(True)

label puzzle_start:
    window hide  # сховати діалогове вікно під час гри

    while True:
        $ reset_puzzle()
        show screen puzzle_minigame
        $ ui.interact()  # чекаємо на взаємодію

        if player_sentence == correct_sentence:
            $ puzzle_solved = True
            hide screen puzzle_minigame
            window show  # повернути діалогове вікно
            jump puzzle_success
        else:
            hide screen puzzle_minigame

label puzzle_success:
    return
