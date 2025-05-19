default map_intro_shown = False

# Вступна кнопка
screen show_screenMap_intro():
    default map_button_enabled = True
    modal True
    add Solid("#00000088")
    frame:
        xalign 0.5
        yalign 0.5
        textbutton "Показати мапу":
            action [Show("map_screen"), Hide("show_screenMap_intro")]

# Кутова кнопка
screen show_screenMap_corner():
    default map_button_enabled = True

    if map_button_enabled:
        frame:
            xalign 1.0
            yalign 0.0
            textbutton "Мапа" xalign 0.5 yalign 0.5 action Show("map_screen")

# Основний екран мапи
screen map_screen():
    modal True
    tag menu
    zorder 100

    # Напівпрозорий фон
    add Solid("#00000088")

    # Локації в одну горизонтальну лінію по центру
    frame:
        xalign 0.5
        yalign 0.5
        background None
        padding (0, 0)
        has hbox spacing 60

        for location in locations:
            $ unlocked = getattr(store, location["unlocked"])
            if unlocked:
                imagebutton:
                    idle location["idle_image"]
                    hover location["hover_image"]
                    at Transform(zoom=0.8)

                    hover_sound "audio/map_hover_unlocked.wav"
                    activate_sound "audio/map_click_available.wav"

                    action [Hide("map_screen"), Jump(location["scene"])]
            else:
                imagebutton:
                    idle "images/locked.png"
                    at Transform(zoom=0.7)

                    hover_sound "audio/map_hover_locked.wav"
                    activate_sound "audio/map_click_locked.wav"

                    action Notify("Ця локація поки що закрита...")

