define hero = Character("Ви", color="#c8ffc8")
init python:
    import random

    # Правильний порядок кольорів
    correct_order = ['red', 'green', 'blue']

    # Початкова генерація випадкового порядку
    def init_puzzle():
        order = ['red', 'green', 'blue']
        random.shuffle(order)
        return order

    # Перевірка, чи порядок правильний
    def check_puzzle(order):
        return order == correct_order

    # Обробка вибору пляшок
    def handle_selection(index):
        if store.puzzle_solved:
            return  # Якщо вже вирішено — блокування

        if store.selected_index is None:
            store.selected_index = index
        else:
            # Обмін місцями
            store.bottle_order[store.selected_index], store.bottle_order[index] = \
                store.bottle_order[index], store.bottle_order[store.selected_index]
            store.selected_index = None

    # Стиль кнопки перевірки
    style.check_button = Style("text_button")
    style.check_button.background = "#444"
    style.check_button.color = "#fff"
    style.check_button.hover_background = "#666"
    style.check_button.hover_color = "#fff"
    style.check_button.padding = (20, 10)


label puzzle_bottles:

    # Ініціалізація змінних перед запуском головоломки
    $ bottle_order = init_puzzle()
    $ selected_index = None
    $ puzzle_solved = False
    $ check_failed = False

    # Відкриття головоломки
    call screen bottle_puzzle

    # Якщо головоломка вирішена — перехід на наступний label
    if puzzle_solved:
        jump puzzle_complete

    return


screen bottle_puzzle():

    tag puzzle

    frame:
        align (0.5, 0.5)
        padding (20, 20, 20, 20)
        has vbox spacing 30

        # Контейнер для пляшок
        frame:
            padding (20, 20, 20, 20)
            xalign 0.5
            yalign 0.5

            hbox:
                spacing 40
                for i, color in enumerate(bottle_order):
                    imagebutton:
                        idle "images/bottles/{}.png".format(color)
                        xysize (600, 600)  # Розмір зображення
                        sensitive not puzzle_solved
                        action Function(handle_selection, i)

        # Кнопка перевірки
        textbutton "Перевірити":
            style "check_button"
            align (0.5, 0.0)
            action [
                If(lambda: check_puzzle(bottle_order),
                    [SetVariable("puzzle_solved", True), SetVariable("check_failed", False)],
                    SetVariable("check_failed", True)
                )
            ]

    # Повідомлення про результат
    if puzzle_solved:
        timer 1.0 action Jump("puzzle_complete")
    elif check_failed:
        text "Неправильно, спробуй ще раз." xpos 0.5 ypos 0.8 size 30 color "#f00"

label puzzle_complete:
    hero "На мапі заблимала інша мітка"
    $ location3_unlocked = True
    $ location2_unlocked = False
    call screen show_screenMap_corner

label go_to_location3:
    if not visited_location3:
        stop music
        scene black with fade
        jump location3_scene_first
    else:
        jump location3_scene

label location3_scene_first:
    jump act3_start
    $ location3_unlocked = True
    $ visited_location3 = True
