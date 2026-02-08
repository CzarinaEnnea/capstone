default player_hp = 100
default bug_hp = 100
default console_text = "Waiting..."

screen battle_ui():

    tag battle

    add "battle_bg"

    # PLAYER
    add "knight" xpos 300 ypos 420

    # BUG
    add "bug" xpos 900 ypos 420

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
        xpos 40
        ypos 300
        xsize 350
        ysize 200

        text "BROKEN CODE / QUESTION"

    # CONSOLE
    frame:
        xpos 0
        ypos 650
        xsize 1280
        ysize 120

        text console_text xalign 0.5 yalign 0.5

label battle:

    show screen battle_ui
    $ console_text = "Grid lines light up."
    $ console_text = "Status panels appear."
    $ console_text = "{color=#32CD32}{b}TURN-BASED LOGIC ENGAGED{/b}{/color}"
    # $ console_text = luna "{b}WAIT—{w}this looks like a game!!{/b}"

    return
