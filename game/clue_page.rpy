screen clue_page():
    modal True  # Блокує взаємодію з фоном
    frame:
        padding (30, 30)
        background "#2228"
        align (0.5, 0.5)

        vbox:
            spacing 15
            text "Підказка зі старої книги" size 32
            text "«1873. Початок. Джерела знання досі спочивають у тіні архівів...»" size 24

            textbutton "Закрити" action Return() xalign 0.5

