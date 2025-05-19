image luna neutral = "ch_luna_neutral.png"
image steven neutral = "ch_steven_neutral.png"

default show_message = True

define l = Character("Luna")
define s = Character("Steven")

screen hottub():
    add "hottubtest"
    modal True

    imagebutton auto "hottubtest_knob_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Temperature control")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("knob")

    imagebutton auto "hottubtest_towel_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Towel")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("towel")

    imagebutton auto "hottubtest_tree_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip", "Tree")
        unhovered SetVariable("screen_tooltip", "")
        action Jump("tree")

label start11:

    scene hottubtest

    label hottub:
        call screen hottub

    label knob:
        "This is the temp control for the hottub."
    jump hottub
    
    label towel:
        "This is a towel."
    jump hottub

    label tree:
        "This is a tree."
    jump hottub

    return
