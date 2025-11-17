label string_leech:
    $ WC_local = 0  # local attempt counter

    while True:
        $ answer = renpy.input('#Overwhelm the bug with more bug \nMultiply the BUG string into 0').strip()

        if answer == 'print("BUG" * 0)':
            play music right_answer noloop
            "Correct! \n{color=#32CD32}{b}print(\"BUG\" * 0){/b}{/color}"
            "The Bug vanishes into thin air"
            hide screen info_box
            hide bug with dissolve
            "Bug Defeated! \nNice job! That is the right code."
            show cyra happy
            cyra "Multiplied by zero will always be ZERO. Well done [name]!!!"
            hide cyra happy
            show cyra neutral at right
            kai "hmp...."
            show kai neutral
            kai "That was nothing."
            return

        else:
            $ WC_local += 1
            if WC_local == 1:
                show cyra sad
                show kai sad
                cyra "Remember [name], the BUG is a string....use double quotation!"
                hide cyra sad
                show cyra neutral at right
            if WC_local >= 3:
                play music error_wrong noloop
                "You have reached the maximum attempts."
                "The Bug Leech Attack"
                "{color=#ff4444}{b}TEAM [name] -1{b}{color=#ff4444}"
                show cyra angry
                show kai angry
                show red
                pause 1
                $ change_confidence(-1)
                cyra "AHhh!"
                kai "uhhh"
                mc "Sorrryyyy"
                kai "FOCUS [name]!"
                show kai angry2
                kai "We lose a point for that."
                hide red
                hide bug
                hide cyra angry
                hide kai angry
                show cyra neutral at right
                show kai neutral
                return  # or jump somewhere else if you want
            else:
                play music error_sound1 noloop
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."
