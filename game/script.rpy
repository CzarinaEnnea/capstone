# TODO: Change color of chara names. Kai/Cyra also have color names in ep1 change it too

# PLACEHOLDERS: Delete when art assets are finished
image arena = Placeholder("bg")
image futuristic skyline = Placeholder("bg")
image cafe = Placeholder("bg")

image doctorbyte = Placeholder("boy")
image kai = Placeholder("boy")
image cyra = Placeholder("girl")
image mspython = Placeholder("girl")
image luna = Placeholder("girl")
image astra = Placeholder("girl")
image mira = Placeholder("girl")




# Characters
define cyra = Character("Cyra", color="#a14ae9")
define mc = Character("[name]", color="#db345d")
define dr = Character("Dr. Byte", color="#61f0dd")
define drIntercom = Character("Dr. Byte (Through Intercom)", color="#61f0dd")
define mspy = Character("Ms. Py Thon", color="#8ef061")
define mspyIntercom = Character("Ms. Py Thon’s Voice Over Intercom", color="#8ef061")
define luna = Character("Luna", color="#e2f061")
define astra = Character("Astra", color="#f061c5")
define kai = Character("Kai", color="#618ef0")
define mira = Character("Mira", color="#f8a3c7")

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

# Customized Transformations
transform top_left_space:
    xalign 0.0
    yalign 0.0
    ypos 100  
    xpos 100

transform top_right_space:
    xalign 1.0      
    yalign 0.0      
    ypos 100       
    xpos 1820

transform slightleft:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.75
    yalign 1.0

# $ red_effect()
init python:
    def red_effect(trans1=pixellate, trans2=dissolve):
        renpy.show("red")
        renpy.with_statement(trans1)
        renpy.hide("red")
        renpy.with_statement(trans2)

# Custom sprite animation
image mspython vhappy:    
    "mspython happy"
    ypos 1.0
    linear 0.21 ypos 1.05
    linear 0.17 ypos 1.0 
    pause 0.48
    "mspython happy"
    ypos 1.0 

transform rise_up:
    ypos 1.0        
    xalign 0.5      
    linear 0.5 ypos 0.0

# Default Variables
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

# Dialogue Styles
init python:
    style.red = Style(style.say_dialogue)
    style.red.color = "#ff3e3e"
    style.red.italic = True

init python:
    style.gold = Style(style.say_dialogue)
    style.gold.color = "#fff346"
    style.gold.italic = True

init python:
    style.code = Style(style.say_dialogue)
    style.code.color = "#81f08aff"
    style.code.italic = True
    style.code.size = 55 

screen info_box(text):
    frame:
        background "#222222aa"
        xpadding 25
        ypadding 15
        xalign 0.05
        yalign 0.05
        text text size 40 color "#00ffcc"

# Functions to change Flags
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

# Start Game
label start:
    call episode0 from _call_episode0
    call episode1 from _call_episode1
    call episode2 from _call_episode2
    # call episode3
    # call episode4
    # call episode5
    # call episode6
    # call episode7
    # call episode8
    
    return