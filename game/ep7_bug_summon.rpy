default mira_fate = 0

label bug_summon_phase1:
    if female == True:
        show female2-pixel with dissolve:
            subpixel True pos (0.25, 0.25) zoom 1.81
    else:
        show male2-pixel with dissolve:
            subpixel True pos (0.25, 0.25) zoom 1.81

    $ console_text = "Enemy Effect: Regenerates every turn unless stopped correctly"
    with dissolve
    ""
    mspy2 neutral "Choose wisely."
    mspy2 neutral "You are not attacking—"
    mspy2 neutral "You are {b}changing behavior.{/b}"

    $ question_text = "while loop_active: {p}{space=40}______________"
    $ console_text = "Look at the Panel and type the missing code"
    with dissolve
    ""
    # input+question
    $ WC_local = 0

    while True:
        $ answer = renpy.input('Type the missing code:').strip()

        if answer == "loop_active = False":
            $ mira_fate += 1

            play sound "right_answer.ogg"
            "{color=#32CD32}{b}CORRECT!{/b}{/color}"
            play sound punch_sound2
            with hpunch
            $ bug_hp = 30
            $ console_text = "The Loopling freezes, then dissolves"
            with dissolve
            ""
            play sound hologram
            hide stringleech-pixel with dissolve
            ""

            mira2 surprised-nosign "…You didn’t delete it."
            scene black
            with dissolve
            return

        else:
            $ WC_local += 1
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                "{color=#ff4444}{b}You have reached the maximum attempts.{/b}{/color}"
                play sound "glitch_sound.ogg"
                call pixel_flash
                $ player_hp = 10
                with vpunch
                $ console_text = "Loopling duplicates"
                with dissolve
                
                show stringleech-pixel as clone1 with dissolve:
                    subpixel True pos (0.58, 0.35) zoom 2.0 

                ""
                $ console_text = "Academy stability –10%"
                with dissolve
                ""
                scene black
                with dissolve
                return

            if WC_local == 1:
                mspy2 neutral "What makes repetition stop?"
            if WC_local == 2:
                cyra2 sad "Don’t overpower it, contain it."
                play sound "error_sound1.ogg"
                call pixel_flash
                $ player_hp = 25
                with dissolve
                "Try again! You have [3 - WC_local] attempt(s) left."
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"

                call pixel_flash

                $ console_text = "YOU TOOK DAMAGE!"
                $ player_hp = 75
                with dissolve
                "Try again! You have [3 - WC_local] attempt(s) left."
    return

label bug_summon_phase2:
    $ console_text = "The bug multiplies when accessed incorrectly."
    ""

    if female == True:
        show female2-pixel with dissolve:
            subpixel True pos (0.25, 0.25) zoom 1.81
    else:
        show male2-pixel with dissolve:
            subpixel True pos (0.25, 0.25) zoom 1.81

    # input+question
    $ question_text = "if data_exists: {p}{space=40}______________"
    with dissolve

    $ WC_local = 0

    while True:
        $ answer = renpy.input('Type the missing code: Store safely using a condition').strip()

        if answer == "preserve(data)":
            $ mira_fate += 1

            play sound "right_answer.ogg"
            "{color=#32CD32}{b}CORRECT!{/b}{/color}"
            play sound punch_sound2
            with hpunch
            $ bug_hp = 40
            $ console_text = "Bug calms"
            with dissolve
            ""
            $ console_text = "Fragments reassemble, then fade"
            with dissolve
            ""
            play sound hologram
            hide bugphantom-pixel with dissolve
            ""
            "Mira’s HP does not drop—but her defense lowers."

            mira2 neutral "…You’re keeping it."
            scene black
            with dissolve
            return

        else:
            $ WC_local += 1
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                "{color=#ff4444}{b}You have reached the maximum attempts.{/b}{/color}"
                play sound "glitch_sound.ogg"
                call pixel_flash
                $ player_hp = 10
                with vpunch
                $ console_text = "Bug retaliates"
                with dissolve
                ""
                mira2 sad "You erase too easily."
                $ console_text = "Party stability –10%"
                with dissolve
                ""
                scene black
                with dissolve
                return

            if WC_local == 1:
                cyra2 surprised "Remember [name] we need to preserve DATA."
            if WC_local == 2:
                kai2 angry "[name.upper()] THIS ISN’T A TRAINING ANYMORE TAKE IT SERIOUSLY!!"
                luna2 serious "Calm down Kai its not helping at all."
                astra2 sad "Sigh! [name] Remember as Cyra said before {b}{i}“preserve()”{/i}{/b} what?"
                play sound "error_sound1.ogg"
                call pixel_flash
                $ player_hp = 25
                with dissolve
                "Try again! You have [3 - WC_local] attempt(s) left."
                mira2 happy "You’re on your last try..." 
                mira2 serious "Make it worth."
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                $ console_text = "YOU TOOK DAMAGE!"
                call pixel_flash
                $ player_hp = 75
                with dissolve
                "Try again! You have [3 - WC_local] attempt(s) left."
    return

label bug_summon_phase3:
    $ console_text = "PLAYER TURN — FINAL LOGIC MOVE"
    ""

    if female == True:
        show female2-pixel with dissolve:
            subpixel True pos (0.25, 0.25) zoom 1.81
    else:
        show male2-pixel with dissolve:
            subpixel True pos (0.25, 0.25) zoom 1.81

    # input+question
    $ question_text = "if trust == False: {p}{space=40}wait() {p}______ {p}{space=40}cooperate()"
    with dissolve

    $ WC_local = 0

    while True:
        $ answer = renpy.input('Type the missing syntax:').strip()

        if answer == "else:":
            $ mira_fate += 1

            play sound "right_answer.ogg"
            "{color=#32CD32}{b}CORRECT!{/b}{/color}"
            play sound punch_sound2
            with hpunch
            $ bug_hp = 80
            $ console_text = "Bug lowers its head and vanishes"
            with dissolve
            ""
            play sound hologram
            hide void-pixel with dissolve
            ""
            "Mira stumbles backward."

            mira2 surprised-nosign "…You allowed another outcome."
            hide screen battle_ui
            stop music fadeout 0.5
            scene black
            with dissolve
            pause 3
            return

        else:
            $ WC_local += 1
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                "{color=#ff4444}{b}You have reached the maximum attempts.{/b}{/color}"
                play sound "glitch_sound.ogg"
                call pixel_flash
                $ player_hp = 5
                with vpunch
                kai2 angry2 "She’s reinforcing herself!"
                mspy2 angry2-nosign "Careful—"
                mspy2 angry-nosign "Force creates resistance!"


                $ console_text = "Stability drops"
                with dissolve
                ""
                $ console_text = "Battle becomes harder (but not unwinnable)"
                with dissolve
                ""
                hide screen battle_ui
                stop music fadeout 0.5
                scene black
                with dissolve
                pause 3
                return

            if WC_local == 1:
                kai2 angry2 "Focus on your battle [name], it's a conditional statement!"
                luna2 happy "Uh..hate to ruin this moment for you [name] but, beat that bug already and help me too.. "
                luna2 angry "There’s so many of them!!! Or {b}“ELSE”{/b}"
            if WC_local == 2:
                astra2 sad "That’s your 2nd you only have ONE attempt left [name]."
                cyra2 sad "Relax everyone. [name] come on finish it already."
                kai2 angry "Yea or ELSE I’ll be the one to finish you!"
                play sound "error_sound1.ogg"
                call pixel_flash
                $ player_hp = 20
                with dissolve
                "Try again! You have [3 - WC_local] attempt(s) left."
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                $ console_text = "YOU TOOK DAMAGE!"
                call pixel_flash
                $ player_hp = 60
                with dissolve
                "Try again! You have [3 - WC_local] attempt(s) left."
    return


label pixel_flash:

    if female:
        show female2-pixelred with dissolve:
            subpixel True
            pos (0.25, 0.25)
            zoom 1.81
    else:
        show male2-pixelred with dissolve:
            subpixel True
            pos (0.25, 0.25)
            zoom 1.81

    pause 0.2

    if female:
        hide female2-pixelred with dissolve
    else:
        hide male2-pixelred with dissolve

    return


# MIRA'S FATE
label good_end:
    scene classroom
    show mspython neutral2 at right
    with dissolve
    play music "audio/sad_Sadness and Solo-8 Bit Lofi Hip Hop.ogg" fadein 0.5 volume 0.8

    "Ms. Py Thon steps forward, calm and resolute."
    show mspython neutral
    mspy "Mira, you will stay."
    show mspython neutral2
    show mira sad2 at center with dissolve
    "Mira stiffens."
    show mspython neutral
    mspy "But not as an Architect."
    show mspython neutral2
    "A pause."
    "Then—{w}warmth."

    show mspython happy with dissolve
    mspy "As a student."
    show mspython happy2

    show mira surprised2
    "Mira’s eyes widen."
    show mira surprised
    mira "{cps=30}…You’re letting me {w}rewrite myself?"
    mc "Everyone deserves refactoring."

    show mira happy2 with dissolve
    "Mira bows her head—not in shame."
    show mira happy with dissolve
    "In relief."

    show doctorbyte sad at left with dissolve
    dr "I’ll be here. {w}This time."

    scene black
    with fade
    stop music fadeout 1.5
    pause 2.0
    return

label neutral_end:
    scene prison
    with dissolve
    play music "audio/sad_Sadness and Solo-8 Bit Lofi Hip Hop.ogg" fadein 0.5 volume 0.8

    show mira neutral2 at center with dissolve
    "Mira stands behind a transparent barrier in a restricted lab."
    "Not imprisoned."
    "Contained."

    show mira neutral
    mira "I’ll observe."
    mira "I’ll learn… {w}quietly."
    show mira neutral2

    "She meets [name]’s eyes."
    show mira happy with dissolve
    mira "Thank you for not deleting me."
    hide mira with dissolve
    "The door closes."
    "But the lights stay on."

    scene black
    with fade
    stop music fadeout 1.5
    pause 2.0

    return

label bad_end:
    scene prison
    with dissolve
    play music "audio/sad_Sadness and Solo-8 Bit Lofi Hip Hop.ogg" fadein 0.5 volume 0.8

    show mira neutral2 at center with dissolve
    
    "Mira’s access keys deactivate."
    "No struggle."
    "No anger."

    show mira neutral
    mira "So this is what clean code feels like."
    "The screen fades quickly."
    hide mira with dissolve
    pause 1.5

    nvl clear
    mcNVL "The system survived." with dissolve
    mcNVL "Something human didn’t." with dissolve

    scene black
    with dissolve
    stop music fadeout 1.5
    pause 2
    nvl clear
    return