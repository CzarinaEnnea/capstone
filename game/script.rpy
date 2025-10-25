# TODO: Change color of chara names
define cyra = Character("Cyra", color="#a14ae9")
define mc = Character("[name]", color="#db345d")
define dr = Character("Dr. Byte", color="#61f0dd")
define mspy = Character("Ms. Py Thon", color="#8ef061")
define luna = Character("Luna", color="#e2f061")
define astra = Character("Astra", color="#f061c5")

define us = Character(
    None,
    window_background=None,
    what_outlines=[(4, "#493f9c", 0, 0)],
    what_size=28,
    what_xalign=0.5,
    what_textalign=0.5,
    #what_layout='subtitle',
    what_bold=True
)

transform top_left_space:
    xalign 0.0
    yalign 0.0
    ypos 100  
    xpos 100

# transform top_right_space:
#     xalign 1.0      
#     yalign 0.0      
#     ypos 100       
#     xpos -100

default syntaxConfidence = 0
default kaiAffection = 0
default cyraAffection = 0
default name = ""
default female = False
default male = False
default They = "They"
default they = "they"
default Them = "Them"
default them = "them"
default Their = "Their"
default their = "their"
default Theirs = "Theirs"
default theirs = "theirs"
default Theyre = "They're"
default theyre = "they're"
default Ms = ""

init python:
    style.red = Style(style.say_dialogue)
    style.red.color = "#ff3e3e"
    style.red.italic = True

init python:
    style.gold = Style(style.say_dialogue)
    style.gold.color = "#fff346"
    style.gold.italic = True

# Function to change Flags
init python:
    def change_confidence(amount):
        global syntaxConfidence
        syntaxConfidence = max(0, syntaxConfidence + amount)

init python:
    def change_kaiAffection(amount):
        global kaiAffection
        kaiAffection = max(0, kaiAffection + amount)

init python:
    def change_cyraAffection(amount):
        global cyraAffection
        cyraAffection = max(0, cyraAffection + amount)

label start:
    call episode0
    call episode1
    # call episode2
    # call episode3
    # call episode4
    # call episode5
    # call episode6
    # call episode7
    # call episode8










    

    # "You are running trying to find your room."

    # scene salon
    # show ryo
    # with dissolve

    # "???" "Someone is in this room maybe I can ask her for directions."

    # c "I think you are lost."

    # c "Can I have your name student?"

    # mc "It's [name]"

    # c "You're [name]. Did I heard it right?"

    # mc "Yes!"

    # show text1 at top_left_space
    # with dissolve
    
    # c "Random text here"

    # c "Another random text explaining"

    # hide text1
    # show text2 at top_left_space
    # # with dissolve

    # mc "I see I see.."

    # hide text2

    # c "Look out there are bugs!"

    
    # show red
    # show bug at top_left_space
    # with pixellate
    # hide red
    # with dissolve


    # c "We need to fight it"

    # mc "Bring it on. Hiya!"

    # with vpunch

    # mc "Ey!"

    # with hpunch

    # hide bug
    # with dissolve

    # "Scree{size=-1}eee{/size}{size=-7}echhhh!{/size}"

    # mc "...."


    return
