label bug_phanthom:
    $ WC_local = 0  # local attempt counter

    while True:
        $ answer = renpy.input('Bug = 0 \nWe = 99 \n_________ \n       print("We are stronger!")').strip()

        if answer == "if We > Bug:":
            show cyra happy
            show kai happy2
            play sound "right_answer.ogg"
            "Correct! \n{color=#32CD32}{b}Output: \nWe are stronger!{/b}{/color}"
            show kai happy
            show cyra happy2
            with vpunch
            play sound "punch_sound1.ogg"
            "You threw digital punches at the Bug Phanthom and it vanishes."

            hide screen info_box with dissolve
            play sound "hologram.ogg"
            hide bugPhantom with dissolve

            show cyra happy
            cyra "It's true we are Stronger than that Bug."
            return
        else:
            $ WC_local += 1
            if WC_local == 1:
                show cyra neutral2
                pause 1
                show cyra neutral
                cyra "Remember it starts with \"if\" then your statement."
                show cyra neutral2
            if WC_local >= 3:
                play sound "error_wrong.ogg"
                "{color=#ff4444}{b}FALSE{/b}{/color}"
                "The Booleen Phanthom attacks!"
                show red
                with hpunch
                play sound punch_sound1

                show kai sad
                show cyra sad
                kai "tchh.."
                cyra "aAHhhhh!"
                mc "Owwwwiee!"
                show cyra sad2
                show kai angry2
                kai "You really need to review our lessons [name]."
                show cyra sad
                cyra "[name] for once I agree with Kai."
                
                hide screen info_box with dissolve
                hide bugPhantom with dissolve
                return  # or jump somewhere else if you want
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."
