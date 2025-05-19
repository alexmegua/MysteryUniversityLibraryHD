screen object_interaction():
    modal True
    frame:
        background "#0008"
        align (0.5, 0.5)
        padding (40, 40)

        vbox:
            spacing 20
            text "Ти оглядаєш полиці..."
            textbutton "Знайти підказку" action [Hide("object_interaction"), SetVariable("clue_found", True), Return()]
