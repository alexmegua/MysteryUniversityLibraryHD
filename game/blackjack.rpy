# Define audio
define audio.card_sound = "card_deal.mp3"
define audio.win_sound = "win.mp3"
define audio.lose_sound = "lose.mp3"

# Define images
image bg table = "bg_table.jpg"
image card_back = "card_back.png"

# Full deck (52 cards)
default deck = [
    "A_of_spades", "2_of_spades", "3_of_spades", "4_of_spades", "5_of_spades", "6_of_spades", 
    "7_of_spades", "8_of_spades", "9_of_spades", "10_of_spades", "J_of_spades", "Q_of_spades", "K_of_spades",
    "A_of_hearts", "2_of_hearts", "3_of_hearts", "4_of_hearts", "5_of_hearts", "6_of_hearts", 
    "7_of_hearts", "8_of_hearts", "9_of_hearts", "10_of_hearts", "J_of_hearts", "Q_of_hearts", "K_of_hearts",
    "A_of_diamonds", "2_of_diamonds", "3_of_diamonds", "4_of_diamonds", "5_of_diamonds", "6_of_diamonds", 
    "7_of_diamonds", "8_of_diamonds", "9_of_diamonds", "10_of_diamonds", "J_of_diamonds", "Q_of_diamonds", "K_of_diamonds",
    "A_of_clubs", "2_of_clubs", "3_of_clubs", "4_of_clubs", "5_of_clubs", "6_of_clubs", 
    "7_of_clubs", "8_of_clubs", "9_of_clubs", "10_of_clubs", "J_of_clubs", "Q_of_clubs", "K_of_clubs"
]

# Enhanced animations
transform card_fancy_deal(start_x, start_y, end_x, end_y):
    xpos start_x ypos start_y alpha 0.0 rotate 0
    parallel:
        linear 0.7 xpos end_x ypos end_y
    parallel:
        linear 0.5 rotate 360
    parallel:
        linear 0.3 alpha 1.0

transform card_flip:
    linear 0.3 rotate 90
    linear 0.3 rotate 0

transform card_bounce:
    linear 0.2 ypos -20
    linear 0.2 ypos 0

# Helper function to calculate score
init python:
    def calculate_score(hand):
        score = 0
        aces = 0
        
        for card in hand:
            value = card.split("_")[0]
            if value in ["J", "Q", "K"]:
                score += 10
            elif value == "A":
                aces += 1
            else:
                score += int(value)
                
        for _ in range(aces):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1
                
        return score

# Game screen
screen blackjack_screen():
    add "bg table" zoom 1.0
    
    # Display scores
    text "Player: [player_score]" xpos 50 ypos 50 size 40
    if game_over:
        text "Dealer: [calculate_score(dealer_hand)]" xpos 50 ypos 120 size 40
    else:
        text "Dealer: [calculate_score([dealer_hand[0]])]" xpos 50 ypos 120 size 40
    
    # Player cards
    for i, card in enumerate(player_hand):
        if renpy.loadable(card + ".png"):
            add "[card].png" at card_fancy_deal(960, -200, 710 + (i * 150), 700) zoom 0.75
    
    # Dealer cards
    for i, card in enumerate(dealer_hand):
        if i == 0 or game_over:
            if renpy.loadable(card + ".png"):
                add "[card].png" at card_fancy_deal(960, -200, 710 + (i * 150), 200) zoom 0.75
        else:
            add "card_back" at card_fancy_deal(960, -200, 710 + (i * 150), 200) zoom 0.75
    
    # Buttons
    if not game_over:
        textbutton "Hit" xpos 780 ypos 800 text_size 50 action Jump("hit") xsize 200 ysize 80
        textbutton "Stand" xpos 980 ypos 800 text_size 50 action Jump("stand") xsize 200 ysize 80

# Game logic
label start1:
    "Welcome to Blackjack!"
    jump start_round

label start_round:
    python:
        current_deck = deck.copy()  # Создаем копию колоды
        renpy.random.shuffle(current_deck)  # Перемешиваем копию
        player_hand = []
        dealer_hand = []
        game_over = False
        player_score = 0
    
    # Initial deal
    play sound card_sound
    $ player_hand.append(current_deck.pop())
    pause 0.5
    play sound card_sound
    $ dealer_hand.append(current_deck.pop())
    pause 0.5
    play sound card_sound
    $ player_hand.append(current_deck.pop())
    pause 0.5
    play sound card_sound
    $ dealer_hand.append(current_deck.pop())
    
    $ player_score = calculate_score(player_hand)
    
    show screen blackjack_screen
    return

label hit:
    python:
        if current_deck:  # Проверяем, есть ли карты в колоде
           
            player_hand.append(current_deck.pop())
            player_score = calculate_score(player_hand)
            
            if player_score > 21:
                game_over = True
                renpy.say(None, "Bust! You lose!")
                renpy.play(audio.lose_sound)
                renpy.jump("end_game")
    return

label stand:
    $ game_over = True
    # Dealer plays
    while calculate_score(dealer_hand) < 17 and current_deck:
        play sound card_sound
        $ dealer_hand.append(current_deck.pop())
        pause 0.7
    
    $ dealer_score = calculate_score(dealer_hand)
    show screen blackjack_screen
    
    if dealer_score > 21:
        "Dealer busts! You win!"
        play sound win_sound
    elif dealer_score > player_score:
        "Dealer wins! [dealer_score] vs [player_score]"
        play sound lose_sound
    elif dealer_score < player_score:
        "You win! [player_score] vs [dealer_score]"
        play sound win_sound
    else:
        "Tie game!"
        play sound card_sound
    
    jump end_game

label end_game:
    pause 2.0
    hide screen blackjack_screen
    menu:
        "Play again?"
        "Yes":
            jump start_round
        "No":
            return