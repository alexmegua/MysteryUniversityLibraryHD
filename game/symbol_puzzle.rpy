# Вставте цей код у файл script.rpy

label start_p:

    scene bg room

    "Перед вами старовинна плита з трьома обертовими кільцями."
    "Щоб відкрити двері, потрібно обернути кільця так, щоб лінії збігалися з малюнком із книги."

    call screen puzzle_screen

    return


# Параметри головоломки
default ring1 = 0
default ring2 = 0
default ring3 = 0
# Рішення головоломки
define solution = (1, 2, 3)  # наприклад, правильні оберти: 1, 2, 3

screen symbol_puzzle():

    frame:
        xalign 0.5
        yalign 0.5
        has vbox

        text "Оберіть позиції кілець" size 30

        hbox:
            spacing 50

            vbox:
                text "Кільце 1: [ring1]" size 20
                textbutton "Обертати" action SetVariable("ring1", (ring1 + 1) % 4)

            vbox:
                text "Кільце 2: [ring2]" size 20
                textbutton "Обертати" action SetVariable("ring2", (ring2 + 1) % 4)

            vbox:
                text "Кільце 3: [ring3]" size 20
                textbutton "Обертати" action SetVariable("ring3", (ring3 + 1) % 4)

        textbutton "Перевірити" action Function(check_puzzle)


init python:
    def check_puzzle():
        if (ring1, ring2, ring3) == solution:
            renpy.hide_screen("puzzle_screen")
            renpy.call_in_new_context("puzzle_solved")
        else:
            renpy.notify("Невірна комбінація. Спробуйте ще.")

label puzzle_solved:

    "Ви чуєте глухий щелчок..."
    "Двері починають повільно відкриватися з металевим скреготом."

    return
