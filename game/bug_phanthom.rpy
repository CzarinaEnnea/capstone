label bug_phanthom:
    $ WC_local = 0  # local attempt counter

    while True:
        $ answer = renpy.input('Bug = 0 \nWe = 99 \n_________ \n       print("We are stonger!")').strip()


        if answer == "if We > Bug:":
            show cyra happy
            show kai happy2
            play music right_answer noloop
            "Correct! \n{color=#32CD32}{b}Output: \nWe are stronger!{/b}{/color}"
            show kai happy
            show cyra happy2
            "You threw digital punches at the Bug Phanthom and it vanishes."
            hide bugPhantom
            show cyra happy
            cyra "It's true we are Stronger than that Bug."
            show cyra neutral2
            show kai neutral2
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
                play music error_wrong noloop
                "{color=#ff4444}{b}FALSE{/b}{/color}"
                "The Booleen Phanthom attacks!"
                show red
                play music punch_sound1 noloop
                show kai sad
                show cyra sad
                kai "tchh.."
                cyra "aAHhhhh!"
                mc "Owwwwiee!"
                show kai angry2
                kai "You really need to review our lessons [name]."
                cyra "[name] for once I agree with Kai"
                show kai neutral2
                show cyra neutral2
                hide bugPhantom with dissolve
                return  # or jump somewhere else if you want
            else:
                play music error_sound1 noloop
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."
