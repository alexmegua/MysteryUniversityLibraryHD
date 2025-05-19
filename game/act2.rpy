define cat = Character("Сін", color="#ffc8c8")
define cat_secret = Character("Кіт", color="#ffc8c8")
define hero = Character("Ви", color="#c8ffc8")

default grid_width = 3
default grid_height = 3
define puzzle_field_size = 650
define puzzle_field_offset = 30
define puzzle_piece_size = 450
define grip_size = 75
define active_area_size = puzzle_piece_size - (grip_size * 2)
define slow_dissolve = Dissolve(1.0)

default location1_unlocked = False # Змінні: чи доступна локація
default location2_unlocked = False
default location3_unlocked = False
default location4_unlocked = False

default visited_location1 = False  # Змінні: чи вперший раз персонаж на локації (Дві різні label)
default visited_location2 = False  
default visited_location3 = False  
default visited_location4 = False  

define locations = [
    {
        "name": "location1",
        "unlocked": "location1_unlocked",
        "idle_image": "images/gui/location1_idle.png",
        "hover_image": "images/gui/location1_hover.png",
        "scene": "go_to_location1",
        "xalign": 0.4,
        "yalign": 0.2
    },
    {
        "name": "location2",
        "unlocked": "location2_unlocked",
        "idle_image": "images/gui/location2_idle.png",
        "hover_image": "images/gui/location2_hover.png",
        "scene": "go_to_location2",
        "xalign": 0.77,
        "yalign": 0.75
    },
        {
        "name": "location3",
        "unlocked": "location3_unlocked",
        "idle_image": "images/gui/location3_idle.png",
        "hover_image": "images/gui/location3_hover.png",
        "scene": "go_to_location3",
        "xalign": 0.5,
        "yalign": 0.3
    },
        {
        "name": "location4",
        "unlocked": "location4_unlocked",
        "idle_image": "images/gui/location4_idle.png",
        "hover_image": "images/gui/location4_hover.png",
        "scene": "go_to_location4",
        "xalign": 0.6,
        "yalign": 0.4
    }
]


# The game starts here.
label act2_start:
    scene paralel_5_hall_mid with fade
    $ screen_tooltip = ""

    show text "..." at center with dissolve

    narrator "Це місце… наче бібліотека, але тут усе занадто… стерильно. Аж нереально. Ні пилу, ні руху. Повітря важке, як перед грозою. Наче я під водою."

    show cat_sleep at right with dissolve

    narrator "Він… не зник. Просто дивиться…"

    hide cat_sleep
    show cat_kill at right

    cat_secret "Ну що, двоногий, дійшло нарешті? Ти більше не вдома. І просто так звідси не вийдеш."

    narrator "Він знову говорить… Це точно не сон?.."

    show hero_confusing at left
    hero "Де я? І хто ти взагалі?"

    cat "Де — не має значення. А я… місцевий хранитель. Називай мене Сін. І так, я не просто кіт."

    hide cat_kill
    show cat_sleep at right

    cat "Хочеш знайти вихід? Тоді дивись уважно. Книга перед тобою — твій перший ключ."

    hide cat_sleep
    hide hero_confusing

    scene paralel_5_1_close_book with dissolve

    narrator "Це вона… Знову. І знову нічого не пояснює."

    narrator "За вікнами — нічого. Жодної будівлі, жодного неба. Лише це світло… Хтось дивиться на мене?.."

    narrator "Сидіти тут без руху — марно. Треба зрозуміти, що це за місце… може, я щось пропустив."

    narrator "Полички... ніби нові. Все стоїть надто рівно. І тиша… така, що хочеться закрити вуха. Але найбільше — ці вікна…"

    scene paralel_6_hall_end with dissolve

    menu:
        "Подивитися в вікно":
            play sound "audio/footsteps_wood.wav"
            jump flash_and_transition
    return  

label flash_and_transition: # Флешка після тицання вікна

    scene white with dissolve
    with Pause(0.4)

    scene black with fade

    narrator "Яке ж воно яскраве!"
    narrator "Ніби блискавка прямо в очі… Що це було?"
    play sound "audio/footsteps_wood.wav"
    pause 2.0

    scene paralel_6_hall_end with fade

    narrator "Тепер видно краще…"
    narrator "Ніякого міста, жодного неба… Просто… ніщо..."
    "Порожнеча."
    play sound "audio/footsteps_wood.wav"
    jump after_flash

    return  

label after_flash:

    scene paralel_5_1_close_book with fade
    play sound "audio/bookflick.wav"
    narrator "Стіл з відкритою книгою. Текст на сторінках рухається, ніби живий, складаючись у химерні візерунки."

    hero "Очі досі палають… Але принаймні тепер я знаю — за вікнами нічого."
    pause 0.5
    hero "Просто сліпа біла порожнеча."

    cat "Ну? Надивився? Може, вже повернемось до важливого, двоногий?"

    hide cat_sleep

    narrator "На столі лежить та сама книга, що перенесла вас сюди. Вона ніби пульсує — дихає."
    hero "Це вона. Та сама. І знову тут. Але тепер… вона чекає?"

    cat "Вона не кусається. Поки що. Відкрий її. Подивимось, чи є в тобі хоч крапля розуму."

    show screen book_interaction
    $ renpy.pause(hard=True)

    hide cat_sleep

    return


screen book_interaction():
    imagebutton:
        idle "images/icons/book_idle.png"
        hover "images/icons/book_hover.png"
        action [Hide("book_interaction"), Jump("first_puzzle")]
        xpos 0.5
        ypos 0.5
        anchor (0.5, 0.5)
        focus_mask True

label first_puzzle:
    scene paralel_5_1_close_book_blur with fade
    play sound "audio/bookflick.wav"

    narrator "Книга повільно розкривається. Сторінки перегортаються самі, зупиняючись на одній."
    narrator "На ній — фрагменти герба: щит із книгою, синє полум’я, ромбовидний візерунок і рухливі символи: ключ, око, три лінії."

    hero "Герб? Але він розбитий, ніби пазл. Цей ромб… я бачив його на обкладинці. І ці символи… вони живі?"

    show cat_sleep at right

    cat "Ну що, втямив, що до чого? Збери його, якщо мозок не заржавів. Книга любить тих, хто не боїться думати."

    hide cat_sleep

    call puzzle_start # Головоломка збирання фрази з перемішаних слів

    if puzzle_solved:
        play sound "magic_spell.wav"
        narrator "Герб оживає: синє полум’я над книгою ворушиться, ромб блимає, символ ключа підсвічується."
        pause 2
        play sound "writing.wav"
        pause 0.2
        narrator "На сторінці з’являється напис: «Шукай тіні там, де знання ховають правду»."

        hero "Герб… він живий? Це полум’я, цей ромб… ніби дивляться на мене. І цей напис… Тіні? Це щось про архів? А ключ… я бачив його серед символів."

        scene paralel_5_1_close_book with fade

        cat "Непогано для новачка. Але це лише перший крок. Бібліотека велика, а правда ховається в її тінях."

        cat "Хочеш знати більше — шукай. Холи, коридори, читальня, склад… усе тут має свої таємниці. І, може, зазирни до бібліотекаря."

        scene paralel_5_hall_mid with fade

        narrator "Сін зникає між стелажами. Лише відлуння його слів ще висить у повітрі."

        hero "Він пішов… але я відчуваю, що він стежить. Ця бібліотека — ніби дихає. І якщо я хочу вибратися, треба знайти ці тіні…"

        $ location1_unlocked = True

        jump map_room_scene
        return  

label map_room_scene:
    $ location1_unlocked = True
    scene black with fade

    if not map_intro_shown: # Чтоб не пропустив мапу, кнопка по-середині
        show screen show_screenMap_intro
        narrator "Мені краще дослідити цю бібліотеку"
        $ map_intro_shown = True
    else:
        show screen show_screenMap_corner # Після кнопка вкутку

    return

label go_to_location1:
    if not visited_location1:
        scene black with fade
        jump location1_scene_first
    else:
        jump location1_scene
    return  

label location1_scene_first:
    scene librarian_1_enter with Dissolve(2.0)
    $ visited_location1 = True
    hero "Тут… тихо. Занадто тихо. Наче повітря тримає подих. Але кожна річ тут щось бачила."
    scene black with fade
    play sound "audio/footsteps_wood.wav"
    pause 1.5
    scene librarian_3_table with Dissolve(1.0)
    hero "План університету?.. Я ніколи не бачив такої детальної карти. Але щось тут не так…"

    show cat_sleep at right
    cat "Помітив? Вона не зовсім така, якою ти її пам’ятаєш. Бібліотека змінюється. І університет — теж."

    hero "Змінюється?.."
    hero "Але чому?.."
    hero "І як карта це показує?.."
    window hide 
    play sound "magic_spell.wav"
    pause 2
    hero "Що це було?.."
    hero "Він..."
    hero "блиснув?" 
    hero "Цей коридор… веде в лабораторію. Чому саме туди?"

    cat "Місце пам’ятає. І воно показує лише тим, хто слухає. Якщо блимає — значить, там щось лишилося."
    cat "Або хтось."

    hero "Значить… наступний крок — лабораторія."

    cat "Може, й додумаєшся, навіщо тебе туди ведуть. А може, знайдеш ще одну загадку. Підеш?"
    hide cat_sleep with dissolve
    $ location2_unlocked = True
    $ location1_unlocked = False
    call screen show_screenMap_corner
    return

label go_to_location2:
    if not visited_location2:
        scene black with fade
        jump location2_scene_first
    else:
        jump location2_scene
    return  

label location2_scene_first:
    scene lab_1_enter with Dissolve(2.0)
    $ location2_unlocked = True
    $ visited_location2 = True

    narrator "Це місце… інше. Більше не схоже на бібліотеку. Скоріше — на щось… експериментальне."
    scene black with fade
    play sound "audio/footsteps_wood.wav"
    pause 1.5
    scene lab_2_choose with Dissolve(1.0)
    narrator "На одному зі столів ви бачите загадкову сферу, що мерехтить тьмяним світлом. Вона трохи підвішена, ніби зависла над поверхнею."
    
    menu:
        "Подивитися на сферу":
            scene black with fade
            play sound "audio/footsteps_wood.wav"
            pause 1.5
            jump flash_and_transition_lab
    return  

label flash_and_transition_lab: # Флешка після тицання вікна

    scene lab_3_book with fade
    play sound "verymagic.wav"
    pause 2.0
    # Після взаємодії зі сферою
    narrator "'Рівновага — не в словах, а в змішанні.'"

    hero "Що це за штука?.. Нічого не пояснює. Але виглядає так, ніби вона… чекає."

    scene lab_3_1_close

    narrator "Ви бачите на іншому столі три великі алхімічні колби. Від кожної йде легке світіння."

    show cat_sleep at right with dissolve

    cat "О, це він любив. Старий алхімік і його рідини."
    cat "Любив порядок. Як і тиша."

    cat "Бачиш ці кольори?"
    cat "Вони мають знайти свої місця."
    cat "І тільки тоді — буде чистота. І відповідь."

    hide cat_sleep with dissolve

    call puzzle_bottles # Головоломка з колбами

    return

# Інші спроби зайти в лаболаторію
label location2_scene:
    call screen lab_1_enter
    return 
