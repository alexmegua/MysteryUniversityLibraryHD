# Визначення персонажів
define e = Character("Ви", image="hero", color="#c8ffc8")
define a = Character("Кіт", image="cat/cat", color="#ffc8c8")

label start:

    scene bgbase
    play music "audio/relaxguitar.wav" fadein 5.0
    show hero_confusing at left with dissolve
    e "Запізно… Зазвичай у цей час у кампусі вже тихо..."
    hide hero_confusing with dissolve
    "Ви йдете в бік бібліотеки..."
    show hero_disapoint at left with dissolve
    e "Скоріше б знайти потрібну книгу і піти"
    hide hero_disapoint with dissolve
    scene black with fade
    jump library_scene


label library_scene:
    play sound "audio/footsteps_wood.wav"
    scene bg4 with Dissolve(2.0)

    show hero_confusing at left with dissolve
    e "Завжди дивно бачити бібліотеку такою пустою..."
    hide hero_confusing with dissolve

    "У кутку помітний силует бібліотекаря..."

    e "Добре, якщо ніхто не заважатиме, я швидко знайду книгу і піду."

    menu:
        "Підійти до каталогу":
            scene black with fade
            jump catalog_scene

label catalog_scene:
    play sound "audio/footsteps_wood.wav"
    scene bg5 with Dissolve(2.0)

    show hero_think2 at left with dissolve
    e "Так… ось вона"
    play sound "audio/bookreading.wav"
    pause 3
    e "Але…"
    hide hero_think2 with dissolve

    show text "Ця книга видана іншому студенту." with fade
    pause 2
    hide text with dissolve

    e "Ну, звісно. Варто було чекати. Гаразд, може, знайду щось схоже."
    scene black with fade
    play sound "audio/footsteps_wood.wav"
    "Ви йдете в інший відділ..."
    pause 0.5
    jump bookshelf_scene

label bookshelf_scene:
    play sound "audio/footsteps_wood.wav"
    pause 3
    play sound "audio/bookfall.wav"
    pause 1
    scene bg6 with fade 
    "Несподівано з верхньої полиці щось важке зривається й падає просто перед вами — на стіл, зі звуком, який змушує здригнутись."

    e "Що за?...."

    "Ви бачите, що на столі лежить стара книга з дивною обкладинкою. Вона виглядає так, ніби чекала саме на нього. Символи на ній химерні, але щось у них знайоме. У центрі — ромбовидний візерунок, а по краям позолота, що ледь помітно пульсує."
    e "Вона... ніби дихає. І кличе."

    menu:
        "Взяти книгу":
            jump take_book
        "Ігнорувати":
            jump ignore_book

label take_book:

    scene bgbook with fade
    play sound "audio/leather.wav"
    "Ви простягуєте руку..."
    e "Чекайте, вона… сама впала?!"

    "Ви на мить завмирає. Потім повільно закриваєте каталог, відсуваєте його вбік, ніби звільняючи місце. Обережно ставите загадкову книгу по центру стола, не зводячи з неї погляду."

    e "Вона сама мене обрала. Тут… я вже нічого не вирішую."
    jump mysterious_event

label ignore_book:
    scene black with fade
    "Ви відвертаєтьсь, але…"
    play sound "audio/bookfall.wav"
    "Книга сама випадає на підлогу."

    e "Що за… Вона сама впала?!"
    jump mysterious_event

label mysterious_event:
    window hide
    play sound "audio/bookflick.wav"
    scene bgbook with Dissolve(2.0)
    "Сторінки починають перегортатися самі по собі..."
    pause 2.4
    e "Це… неможливо…"

    "Ви не може відірвати погляд..."
    stop music fadeout 2.0
    pause 2.0
    scene white with dissolve
    play sound "audio/sonar.wav" fadein 1.0 fadeout 0.5
    with Pause(0.4)
    scene black with fade
    jump transition_to_parallel_library

label transition_to_parallel_library:
    e "Що за чорт…?"
    scene black with fade
    pause 1.5
    jump Parallel_library

label Parallel_library:

    scene bg10 with fade
    e "Де я?"

    "Ви оглядаєтесь..."
    e "Це… вона. Та сама книга. Але я ж був у темній залі… Я не пам’ятаю, як сів…"

    "Ви обережно озирається навколо. Бібліотека виглядає знайомо, але світла тут забагато. Полиці надто ідеальні, тиша надто густа."

    e "Все ніби те саме… але водночас зовсім інше. Це точно не той самий світ."

    "У цей момент зліва з’являється яскраве світло — м’яка, пульсуюча куля лежала на столі, і трохи далі, позаду неї, сидить створіння."
    "Темне хутро, гострі вуха, жовті очі. Воно тримає в лапах книгу і нерухомо спостерігає."
    "Ви повільно повертаєте голову. Ви зустрічається поглядами."

    e "…Тварина? Кіт?.."

    "Кіт раптом повільно зводиться на дві лапи. Залишивши книгу на купі томів, він неквапливо зістрибує вниз і, майже беззвучно ступаючи, прямує до героя. Його рухи плавні, очі не зводяться з обличчя героя."
    "Коли він підходить ближче, стає зрозуміло — істота зовсім невелика, не більше 20 сантиметрів на зріст. Але щось у його поставі, у впевненості кроку — змушує сприймати його серйозніше, ніж звичайного кота."
    "Кіт зупиняється прямо перед героєм, дивиться вгору і, ніби це найзвичніше в світі, каже:"

    scene bg11 with dissolve
    play music "audio/relaxguitar.wav" fadein 5.0
    a "Чого вилупився? Котів не бачив?"
    "Ви завмираєте. Вираз на обличчі — від подиву до повної розгубленості."
    e "Воно... каже?"

    scene bg12 with dissolve
    a "Ох уже ці новенькі... Ну що, двоногий, думав це просто сон? Якщо хочеш вийти — почни з тієї книги перед собою."
    jump act2_start

label end_scene:

    scene bg3 with fade
    play music mus2 fadein 2.0

    show hero_disapoint at right with dissolve
    "Ти повернувся додому. Це кінець. Ти нічого не дізнався."
    hide hero_disapoint with dissolve
    $ renpy.full_restart()

    return
