# TODO: Battle Scene

# PLACEHOLDERS: Delete when art assets are finished
image groupPhoto = Placeholder("bg")

# image bugOgre = Placeholder("boy")

# Characters
define cyra = Character("Cyra", color="#a14ae9")
define mc = Character("[name]", color="#f061c5")
define dr = Character("Dr. Byte", color="#61f0dd")
define drIntercom = Character("Dr. Byte (Through Intercom)", color="#61f0dd")
define drHologram = Character("Dr. Byte (Hologram)", color="#61f0dd")
define mspy = Character("Ms. Py Thon", color="#8ef061")
define mspyIntercom = Character("Ms. Py Thon’s Voice Over Intercom", color="#8ef061")
define luna = Character("Luna", color="#618ef0")
define astra = Character("Astra", color="#e2f061")
define kai = Character("Kai", color="#db345d")
define mira = Character("Mira", color="#f8a3c7")
define n = Character(None, kind=nvl)
define mcNVL = Character("[name]", color="#f061c5", kind=nvl)

# Characters Side Images
define cyra2 = Character("Cyra", color="#a14ae9", image="cyra")
define mspy2 = Character("Ms. Py Thon", color="#8ef061", image="mspython")
define luna2 = Character("Luna", color="#618ef0", image="luna")
define astra2 = Character("Astra", color="#e2f061", image="astra")
define kai2 = Character("Kai", color="#db345d", image="kai")
define mira2 = Character("Mira", color="#f8a3c7", image="mira")

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
    linear 0.5 ypos 0.21

init:
    transform flip:
        xzoom -1.0

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

init python:
    style.title = Style(style.say_dialogue)
    style.title.font = "RagueDemo-Regular.ttf"
    style.title.size = 50
    # style.title.bold = True

# Screens
screen final_box(text):
    frame:
        background "#222222aa"
        xpadding 25
        ypadding 15
        xalign 0.5
        yalign 0.5
        text text size 40 color "#00ffcc"

screen info_box(text):
    frame:
        background "#222222aa"
        xpadding 25
        ypadding 15
        xalign 0.04
        yalign 0.02
        text text size 40 color "#00ffcc"

screen scoreboard():
    frame:
        background "#222222aa"
        align (0.5, 0.2)
        padding (20, 20)

        vbox:
            spacing 50
            text "{b}Scoreboard{/b}" size 50 xalign 0.5 color "#00ffcc"

            grid 3 4 spacing 40:
                style_prefix "table"

                text "{color=#00ffcc}{size=40}{b}Team{/b}{/size}{/color}"
                text "{color=#00ffcc}{size=40}{b}Result{/b}{/size}{/color}"
                text "{color=#00ffcc}{size=40}{b}Grade{/b}{/size}{/color}"

                text "Astra, Luna, Mira"
                text "All Bugs Eliminated"
                text "{b}A+{/b}"

                text "[name], Cyra, Kai"
                text "Shield Up, 1 Mistake"
                text "{b}A{/b}"

                text "Others"
                text "Mixed results"
                text "{b}B to C{/b}"
            
screen loopTable():
    frame:
        background "#222222aa"
        align (0.5, 0.2)
        padding (20, 20)

        vbox:
            spacing 50
            text "{b}Basic For Loop Syntax{/b}" size 50 xalign 0.5 color "#00ffcc"

            grid 3 4 spacing 40:
                style_prefix "table"

                text "{color=#00ffcc}{size=40}{b}Concept{/b}{/size}{/color}"
                text "{color=#00ffcc}{size=40}{b}Code{/b}{/size}{/color}"
                text "{color=#00ffcc}{size=40}{b}Explanation{/b}{/size}{/color}"

                text "{b}Basic Loop{/b}"
                text "{color=#81f08aff}{b}for i in range(5): {p}{space=138}print(i){/b}{/color}"
                text "{b}Repeats from 0 to 4{/b}"

                text "{b}Custom Start{/b}"
                text "{color=#81f08aff}{b}for x in range(2, 6): {p}{space=138}print(x){/b}{/color}"
                text "{b}Starts at 2, ends at 5{/b}"

                text "{b}Step{/b}"
                text "{color=#81f08aff}{b}for y in range(0, 10, 2): {p}{space=138}print(y){/b}{/color}"
                text "{b}Counts by 2{/b}"

screen whileLoopTable():
    frame:
        background "#222222aa"
        align (0.5, 0.2)
        padding (20, 20)

        vbox:
            spacing 50
            text "{b}While Loop Breakdown{/b}" size 50 xalign 0.5 color "#00ffcc"

            grid 2 5 spacing 40:
                style_prefix "table"

                text "{color=#00ffcc}{size=40}{b}Element{/b}{/size}{/color}"
                text "{color=#00ffcc}{size=40}{b}Purpose{/b}{/size}{/color}"

                text "{color=#81f08aff}{b}i = 1{/b}{/color}"
                text "{b}Starting value{/b}"

                text "{color=#81f08aff}{b}while i <= 3:{/b}{/color}"
                text "{b}Condition checked every loop{/b}"

                text "{color=#81f08aff}{b}print(i){/b}{/color}"
                text "{b}Action repeated{/b}"

                text "{color=#81f08aff}{b}i += 1{/b}{/color}"
                text "{b}Update — prevents infinite loop{/b}"

screen whileLoopTableB():
    frame:
        background "#222222aa"
        align (0.5, 0.2)
        padding (20, 20)

        vbox:
            spacing 50
            text "{b}While Loop Breakdown{/b}" size 50 xalign 0.5 color "#00ffcc"

            grid 2 4 spacing 40:
                style_prefix "table"

                text "{color=#00ffcc}{size=40}{b}Element{/b}{/size}{/color}"
                text "{color=#00ffcc}{size=40}{b}Purpose{/b}{/size}{/color}"

                text "{color=#81f08aff}{b}i = 1{/b}{/color}"
                text "{b}Starting value{/b}"

                text "{color=#81f08aff}{b}while i <= 3:{/b}{/color}"
                text "{b}Condition checked every loop{/b}"

                text "{color=#81f08aff}{b}print(i){/b}{/color}"
                text "{b}Action repeated{/b}"

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

# RPG Animation

transform attack_jump:
    ease 0.15 xoffset 558 yoffset -80   # jump forward + up
    ease 0.1 yoffset 0                  # fall down
    ease 0.15 xoffset 0                 # go back

transform enemy_attack1:
    ease 0.15 xoffset -351
    pause 0.5
    ease 0.15 xoffset 0

transform enemy_attack:
    ease 0.15 xoffset -522 yoffset -80
    ease 0.1 yoffset 0
    pause 0.5
    ease 0.15 xoffset 0

# Start Game
label start:
    
    call episode0 from _call_episode0
    call episode1 from _call_episode1
    call episode2 from _call_episode2
    call episode3 from _call_episode3
    call episode4 from _call_episode4
    call episode5 from _call_episode5
    call episode6 from _call_episode6
    call episode7 from _call_episode7
    call episode8 from _call_episode8
    
    return