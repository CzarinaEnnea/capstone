label ep5_scn2_txt1:
    $ WC_local = 0

    while True:
        $ answer = renpy.input('Type a loop that prints numbers 1 to 3:').strip()

        if answer == "for i in range(1, 4):":
            play sound "right_answer.ogg"
            "{color=#32CD32}{b}CORRECT!{/b}{/color}"
            show mspython happy
            mspy "Correct. Precision matters."
            "{=gold}Syntax Confidence +2{/gold}"
            $ change_confidence(+2)
            hide ep5-scn2-txt1 with dissolve
            return
        else:
            $ WC_local += 1
            if WC_local == 1:
                "Hint: Range starts at 1 and ends with n+1"
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                show mspython sad2
                "You have reached the maximum attempts."
                mira "You forgot the range end… it stops before the last number."
                "{b}Correct Answer: {p}{color=#32CD32}for i in range(1, 4):"
                # "{b}Correct Answer: {p}{color=#32CD32}for i in range(1, 4): {p}{space=138}print(i){/color}{/b}"
                return
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."

    return

label ep5_scn3_txt1:
    $ WC_local = 0

    while True:
        $ answer = renpy.input('What would be the output?').strip()

        if answer == "123":
            play sound "right_answer.ogg"
            "{color=#32CD32}{b}CORRECT!{/b}{/color}"
            "A counter-bot salutes."
            show doctorbyte happy
            dr "Good control."
            # "{=gold}Syntax Confidence +2{/gold}"
            # $ change_confidence(+2)
            return
        else:
            $ WC_local += 1
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                "You have reached the maximum attempts."
                show doctorbyte sad2
                play sound "punch_sound2.ogg"
                "Bot walks into a wall repeatedly."
                play sound "punch_sound2.ogg"
                luna "It’s stuck in a loop of regret!"
                play sound "punch_sound2.ogg"
                "{b}Correct Answer: {p}{color=#32CD32}123"
                return
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."

    return

label ep5_scn3_txt2:
    $ WC_local = 0

    while True:
        $ answer = renpy.input('Fill in the blank:').strip()

        if answer == "2":
            play sound "right_answer.ogg"
            "{color=#32CD32}{b}CORRECT!{/b}{/color}"
            show doctorbyte happy2-flower
            cyra "Nested loops = multiplied effects. Remember that."
            # "{=gold}Syntax Confidence +2{/gold}"
            # $ change_confidence(+2)
            return
        else:
            $ WC_local += 1
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                "You have reached the maximum attempts."
                show doctorbyte sad2
                play sound "glitch_sound.ogg"
                "Creature duplicates rapidly."
                kai "You underestimated nesting."
                "Ms. Py Thon snaps fingers {w}— delete."
                play sound "hologram.ogg"
                "{b}Correct Answer: {p}{color=#32CD32}2"
                return
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."

    return