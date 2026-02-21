default player_hp = 100
default bug_hp = 100
default console_text = "text"
default question_text = "BROKEN CODE / QUESTION"
default round_info = "ROUND 1"
default bug_name = " "
default player_name = " "

screen battle_ui():

    tag battle

    # add "battle_bg"

    # PLAYER SPRITE
    # add "knight" xpos 300 ypos 420

    # BUG SPRITE
    # add "void-pixel":
    #     xpos 0.6 ypos 0.15
    #     xzoom -1.0
    #     zoom 2.0

    # PLAYER HP BOX
    frame:
        xpos 0.04
        ypos 40
        xsize 300
        ysize 50

        vbox:
            spacing 10
            text player_name xalign 0.1
            bar value player_hp range 100 xsize 280

    # BUG HP BOX
    frame:
        xpos 0.8
        ypos 40
        xsize 300
        ysize 50

        vbox:
            spacing 10
            text bug_name xalign 0.1
            bar value bug_hp range 100 xsize 280

    # ROUND INFO
    text round_info xpos 0.43 ypos 40 size 40

    # QUESTION PANEL
    frame:
        xpos 0.04
        ypos 0.2
        xsize 350
        ysize 400

        text question_text:
            xalign 0.1
            yalign 0.5
            size 24
            bold True
            color "#32CD32"

    # CONSOLE / TEXTBOX
    frame:
        xpos 0
        ypos 650
        xsize 1920
        ysize 120
        
        text console_text:
            xalign 0.5 
            yalign 0.5 
            size 32
            bold True
            color "#32CD32"

label battle:
    stop music
    
    scene training-chamber
    with dissolve
    "Grid lines light up."
    "Status panels appear."

    play sound glitch_sound
    show screen battle_ui with pixellate
    $ round_info = "BUG 1 — LOOPLING"
    $ bug_name = "LOOPLING"
    $ player_name = name.upper()
    $ question_text = "while loop_active: {p}{space=40}_________"
    $ console_text = "TURN-BASED LOGIC ENGAGED"
    pause

    ""
    show void-pixel with dissolve:
        xpos 0.6 ypos 0.15
        xzoom -1.0
        zoom 2.0
    luna2 surprised3 "{b}WAIT—{w}this looks like a game!!{/b}"
    kai2 angry2 "…Of course it does."
    cyra2 surprised "She’s not fighting us directly."
    mc "She’s testing us."
    astra2 sad "Mira.."
    mspy2 neutral "Focus everyone."

    "Mira raises her hand calmly."
    mira2 happy "I don’t want to destroy you."
    mira2 happy "I want to {b}correct{/b} you."
    "She snaps her fingers."
    ""
    with vpunch
    mc "Ouch!"
    $ console_text = "YOU TOOK DAMAGE!"
    $ player_hp = 50
    show void-pixel with dissolve:
        xpos 0.6 ypos 0.15
        xzoom -1.0
        zoom 2.0
    mc "That hurts..."
    hide screen battle_ui with dissolve
    return