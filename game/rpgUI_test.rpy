default player_hp = 100
default bug_hp = 100
default console_text = "Waiting..."

screen battle_ui():

    tag battle

    # add "battle_bg"

    # PLAYER
    # add "knight" xpos 300 ypos 420

    # BUG
    add "void-pixel":
        # xpos 0.7 ypos 420
        xpos 0.6 ypos 0.15
        xzoom -1.0
        zoom 2.0


    # PLAYER HP
    frame:
        xpos 0.04
        ypos 40
        xsize 300
        ysize 40

        vbox:
            text "PLAYER HP"
            bar value player_hp range 100 xsize 280

    # BUG HP
    frame:
        xpos .8
        ypos 40
        xsize 300
        ysize 40

        vbox:
            text "BUG HP"
            bar value bug_hp range 100 xsize 280

    # ROUND INFO
    text "ROUND INFO" xpos 0.43 ypos 40 size 40

    # QUESTION PANEL
    frame:
        # xpos 40
        xpos 0.04
        # ypos 300
        ypos 0.2
        xsize 350
        ysize 400

        text "BROKEN CODE / QUESTION" xalign 0.5 yalign 0.5

    # CONSOLE
    frame:
        xpos 0
        ypos 650
        xsize 1920
        ysize 120

        text console_text xalign 0.5 yalign 0.5

label battle:
    stop music
    
    scene training-chamber
    with dissolve
    "Grid lines light up."

    play sound glitch_sound
    show screen battle_ui with pixellate
    # $ console_text = "Grid lines light up."
    # $ console_text = "Status panels appear."
    $ console_text = "{color=#32CD32}{b}TURN-BASED LOGIC ENGAGED{/b}{/color}"
    # $ console_text = luna "{b}WAIT—{w}this looks like a game!!{/b}"

    "Status panels appear."

    return
