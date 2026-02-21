label string_leech:
    $ WC_local = 0  # local attempt counter

    while True:
        $ answer = renpy.input('#Overwhelm the bug with more bug \nMultiply the BUG string into 0').strip()

        if answer == 'print("BUG" * 0)':
            play sound "right_answer.ogg"
            "Correct! \n{color=#32CD32}{b}print(\"BUG\" * 0){/b}{/color}"
            "The Bug vanishes into thin air."
            hide screen info_box with dissolve
            play sound "hologram.ogg"
            hide stringleech with dissolve
            "Bug Defeated! \nNice job! That is the right code."
            show cyra happy
            cyra "Multiplied by zero will always be ZERO. Well done [name]!!!"
            show cyra happy2
            show kai neutral2
            kai "Hmp...."
            show kai neutral
            kai "That was nothing."
            return

        else:
            $ WC_local += 1
            if WC_local == 1:
                show cyra sad
                show kai sad
                cyra "Remember [name], the BUG is a string....use double quotation!"
            if WC_local >= 3:
                play sound "error_wrong,ogg" 
                "You have reached the maximum attempts."
                with hpunch
                play sound "punch_sound2.ogg"
                "The Bug Leech Attack"
                "{color=#ff4444}{b}TEAM [name] -1{b}{color=#ff4444}"
                show cyra angry
                show kai angry
                show red
                pause 1
                $ change_confidence(-1)
                cyra "AHhh!"
                kai "Uhhh"
                mc "Sorrryyyy"
                kai "FOCUS [name]!"
                show kai angry2
                kai "We lose a point for that."
                hide red
                show cyra neutral2
                show kai neutral2
                return  # or jump somewhere else if you want
            else:
                play sound "error_sound1.ogg"
                "{color=#ff4444}{b}Incorrect.{/b}{/color}"
                "Try again! You have [3 - WC_local] attempt(s) left."
