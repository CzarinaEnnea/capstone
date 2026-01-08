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