define hero = Character("Ви", color="#c8ffc8")
define cat = Character("Сін", color="#ffc8c8")
define reflection = Character("Відображення", color="#c8c8ff")

# Переменные для блекджека
default knowledge_sum = 0
default knowledge_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Изображения
image bg storage = "images/bg_storage.jpg"
image bg reading_room = "images/bg_reading_room.jpg"
image bg main_hall = "images/bg_main_hall.jpg"
image bg campus_dawn = "images/campus_dawn.jpg"
image cat_cat = "images/cat_cat.png"
image memory_tree = "images/memory_tree.png"
image book = "images/mystery_book.png"
image reflection = "images/reflection.png"

label act3_start:
    scene bg13 with fade
    play music "audio/happyrelax.wav" fadein 5.0
    
    hero "Ніби потрапив у підсвідомість університету. Тут усе, що не підходить до каталогу. Все, що ніхто не хотів пам'ятати..."
    
    show cat_kill at right
    cat "Пам'ять — штука вибіркова. Але іноді, щоб рухатися далі, доводиться згадати. Навіть те, чого не хочеш."
    
    "Ви знаходите металевий предмет, схожий на ручку ключа."
    
    show hero_confusing at left
    hero "Це... частина механізму? Ніби ключ, але без основи... Підстава для чогось більшого."
    
    cat "Ключ не завжди відкриває двері. Іноді він лише вказує, що двері — десь поруч."

    # Переход к мини-игре
    cat "Спробуй знайти решту частин..."
    hide hero_confusing
    hide cat_kill
    scene black with fade
    play sound "audio/footsteps_wood.wav"
    pause 2.5
    call MemoryGame  # Вызов метки мини-игры из другого файла
    play music "audio/happyrelax.wav" fadein 5.0
    show hero_think2 at left
    # Возвращение после мини-игры
    hero "Готово! Тепер цей ключ має сенс..."
    # Переход в читальный зал

    $ location4_unlocked = True
    $ location3_unlocked = False
    call screen show_screenMap_corner
    hide hero_think2
label go_to_location4:
    if not visited_location4:
        jump location4_scene_first
    else:
        jump location4_scene

label location4_scene_first:
    $ location4_unlocked = True
    $ visited_location4 = True
    scene bg14 with fade
    show hero_think at left
    hero "Це місце... Наче сон. Але я відчуваю — тут усе закінчиться. Або почнеться."
    
    show cat_take_this at right
    cat "Це Древо Спогадів. Воно виросло там, де знання осіли навіки. А ти прийшов сюди не просто так. Ти маєш зробити ще одну ставку."
    hide hero_think
    hide cat_take_this
    scene black with fade
    play sound "audio/footsteps_wood.wav"
    pause 2.5
    # Запуск мини-игры "Блекджек знаний"
    call knowledge_blackjack from _call_knowledge_blackjack
    
    scene bg14 with fade
    
    "Після перемоги дерево починає світитися сильніше, листя кружляє в центр кімнати."
    show hero_confusing at left
    hero "Листя... воно показує шлях? Мовби штовхає мене назад. У хол."
    
    show cat_sleep at right
    cat "Ти зробив свій крок. І тепер — повернись. Туди, де почалась твоя історія. Та книга чекає."
    
    hero "Книга... ТА книга. З неї все почалося. І, можливо... закінчиться?"
    
    $ location1_unlocked = True
    $ location4_unlocked = False
    call screen show_screenMap_corner
    hide hero_confusing
    hide cat_sleep

label location1_scene:
    $ location1_unlocked = False
    # Переход в главный зал
    scene bg15 with fade
    play music "audio/relaxguitar.wav" fadein 5.0
    show hero_confusing at left
    hero "Та сама книга. З неї все почалось. Але тепер... я інший."
    
    "Ви відкриваєте її. Всередині — ілюстрації, стилізовані під живі картини."
    
    hero "Це я... чи... той, ким я міг стати? Або ким ще можу бути?"
    
    show cat_sleep at right
    cat "Ти повернувся до початку, щоб завершити цикл. І... розпочати новий."
    
    hero "Цикл?.. А якщо я не хочу?.. Якщо я не готовий?.."
    
    cat "Це не має значення. Цикл триває незалежно від твоїх страхів. Але вибір — завжди був за тобою."
    hide hero_confusing
    hide cat_sleep
    # Финальный выбор
    scene bg15 with fade
    show cat_take_this at right
    
    cat "Два шляхи. Один — до світу. Інший — до історії. До пам'яті. До самотності."
    cat "Ти можеш піти. І забрати з собою лише тінь цієї книги. Ніхто не дізнається. Все забудеться."
    cat "Або — залишишся. І станеш голосом, який сам почув. Ти — потрібен цьому місцю. Але не як герой. Як той, хто пам'ятає."
    show hero_confusing at left
    hero "А якщо я боюся?"
    
    cat "Бійся. Це нормально. Але вибери. Навіть страх — частина історії."
    
    menu:
        "Залишитися Хранителем":
            jump stay_keeper
        "Піти з бібліотеки":
            jump leave_library

label stay_keeper:
    hide hero_confusing
    hide cat_take_this
    scene paralel_5_hall_mid with fade
    "Ви сідаєте за стіл. Книга закривається. Світло тьмяніє."
    hero "Нехай я зникну — але я залишусь тут, де мої знання потрібні."
    scene black with fade
    stop music
    play sound "audio/ending.wav"
    show text "Історія триває. Твоя роль — почалась." with fade
    pause 2.1
    $ renpy.full_restart()

label leave_library:
    scene night_entrance with fade
    "Ви йдете до виходу, тримаючи ту саму книгу, але вже пусту."
    hero "Тепер я знаю, що вона завжди буде зі мною. Навіть якщо — без слів."
    scene black with fade
    stop music
    play sound "audio/ending.wav"
    show text "Істина не в книгах. Істина — у виборі." with fade
    pause 2.1
    $ renpy.full_restart()

# Мини-игра "Блекджек знаний"
label knowledge_blackjack:
    scene bg16 with fade
    $ knowledge_sum = 0
    $ knowledge_deck = knowledge_cards * 4
    $ renpy.random.shuffle(knowledge_deck)
    
    scene bg16 with fade
    show cat_sleep at right
    
    cat "У тебе буде вибір: збирати знання чи зупинитись, коли відчуєш межу. Як і в житті."
    hide cat_sleep
    while knowledge_sum < 21:
        menu:
            "Взяти ще сторінку":
                $ card = knowledge_deck.pop()
                $ knowledge_sum += card
                hero "Я взяв сторінку з числом [card]. Загальна сума: [knowledge_sum]"
                
                if knowledge_sum > 21:
                    cat "Так от воно — бажання знати все. Але все не потрібно. Все — беззмістовне."
                    $ knowledge_sum = 0
                    $ renpy.random.shuffle(knowledge_deck)
                    jump knowledge_blackjack
                    
            "Зупинитися":
                if knowledge_sum == 21:
                    cat "Ти зібрав рівно стільки, скільки потрібно. Не більше, не менше. Тепер — ти готовий."
                    return
                else:
                    cat "Ти зупинився занадто рано. Спробуй ще."
                    jump knowledge_blackjack
    
    cat "Ти зібрав рівно стільки, скільки потрібно. Не більше, не менше. Тепер — ти готовий."
    return