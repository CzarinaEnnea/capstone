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

label ep5_scn3_txt3:
    $ WC_local = 0

    while True:
        $ answer = renpy.input('Fill in the blank:').strip()

        if answer == "in range(5):":
            play sound "right_answer.ogg"
            show doctorbyte happy2-flower
            "{color=#32CD32}{b}CORRECT!{/b}{/color}"
            luna "DEBUG! DEBUG! DEBUG! I LOVE IT!"
            cyra "Clean loop. No extra noise."
            show doctorbyte happy-flower
            dr "“Excellent. Clear structure. Proper indentation. {w}Well executed!"
            "A small Debug-bot gives [name] a thumbs-up."
            # "{=gold}Syntax Confidence +2{/gold}"
            # $ change_confidence(+2)
            return
        else:
            $ WC_local += 1
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                "{color=#ff4444}{b}Final attempt used.{/b}{/color}"
                show doctorbyte sad2
                play sound "glitch_sound.ogg"
                "{b}Correct Answer: {p}{color=#32CD32}in range(5):"
                return
            if WC_local == 1:
                "{color=#ff4444}{b}Output does not match the requirement.{/b}{/color}"
                mspy "Hint: Use a {b}for loop{/b} and the {color=#32CD32}range(){/color} function."
            if WC_local == 2:
                "{color=#ff4444}{b}The loop structure is incomplete or incorrect.{/b}{/color}"
                show doctorbyte sad
                dr "Hint: Check your {b}indentation{/b} and ensure the loop repeats exactly {b}five times{/b}."
                luna "Five times. Not four. Not forever. Just five."
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."

    return

label ep5_scn5_txt2:
    $ WC_local = 0

    while True:
        $ answer = renpy.input('Type the missing line:').strip()

        if answer == "i += 1":
            play sound "right_answer.ogg"
            hide ep5-scn5-txt2
            show ep5-scn5-txt3 at top_left_space 
            with dissolve
            "{color=#32CD32}{b}CORRECT!{/b}{/color}"
            play sound "glitch_sound.ogg"
            "The portal collapses completely."
            cyra "There. Apocalypse cancelled."
            mspy "Well done. You corrected the control flow."
            play sound "right_answer.ogg"
            "{=gold}Infinite Loop Threat Resolved{/gold}"
            "{=gold}Syntax Confidence +1{/gold}"
            $ change_confidence(+1)
            hide ep5-scn5-txt3 with dissolve
            return

        else:
            $ WC_local += 1
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                "{color=#ff4444}{b}You have reached the maximum attempts.{/b}{/color}"
                play sound "glitch_sound.ogg"
                "The portal stabilizes into a harmless but annoying loop."
                mspy "This is what happens when loops are left unchecked."
                dr "No penalty today—but remember this moment."
                luna "It’s looping forever… I hate it…"
                play sound "hologram.ogg"
                hide ep5-scn5-txt2 with dissolve
                "Ms. Py Thon snaps her fingers. The portal closes."

            
                play sound "error_sound1.ogg"
                "{=red}Instructor Intervention Required{/red}"
                "{=red}Syntax Confidence –2{/red}"
                $ change_confidence(-2)
                "{b}Correct Answer: {p}{color=#32CD32}i += 1"
                return

            if WC_local == 1:
                mspy "What value changes each loop?"
            if WC_local == 2:
                mira "The loop needs a way to move forward…"
                kai "If {color=#32CD32}i{/color} never changes, you’re stuck forever."
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."

    return